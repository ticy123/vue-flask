from flask import Flask, jsonify, request
from elasticsearch import Elasticsearch
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# 初始化Flask应用
app = Flask(__name__)

# 配置Elasticsearch连接信息
es = Elasticsearch(hosts=["localhost"], port=9200)

# 配置MySQL数据库连接信息
engine = create_engine('mysql+mysqlconnector://username:password@localhost:3306/mydb', echo=True)
Base = declarative_base()

# 定义MySQL数据模型
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(120), unique=True)

    def __repr__(self):
        return '<User %r>' % self.name

class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    content = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", backref="articles")

    def __repr__(self):
        return '<Article %r>' % self.title

# 创建MySQL数据表
Base.metadata.create_all(engine)

# 初始化SQLAlchemy会话
Session = sessionmaker(bind=engine)
session = Session()

# 添加用户和文章数据到MySQL
user = User(name='John Doe', email='johndoe@example.com')
session.add(user)
session.commit()

article = Article(title='Hello World', content='This is my first article', user_id=user.id)
session.add(article)
session.commit()

# 添加文章数据到Elasticsearch
es.index(index='articles', doc_type='article', id=article.id, body={
    'title': article.title,
    'content': article.content,
    'user_id': article.user_id
})

# 实现API接口，查询MySQL中的文章数据，并从Elasticsearch中获取相应的搜索结果
@app.route('/articles', methods=['GET'])
def search_articles():
    q = request.args.get('q')
    if q:
        # 在Elasticsearch中查询匹配的文章数据
        res = es.search(index='articles', body={
            'query': {
                'match': {
                    'content': q
                }
            }
        })

        # 根据搜索结果获取MySQL中对应的文章数据
        article_ids = [hit['_id'] for hit in res['hits']['hits']]
        articles = session.query(Article).filter(Article.id.in_(article_ids)).all()
    else:
        # 查询所有文章数据
        articles = session.query(Article).all()

    # 返回文章数据
    return jsonify([{
        'id': article.id,
        'title': article.title,
        'content': article.content,
        'user_id': article.user_id,
        'user_name': article.user.name
    } for article in articles])




# 启动Flask应用
if __name__ == '__main__':
    app.run(debug=True)
