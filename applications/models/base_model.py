from applications.extensions.init_db import db

class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='标识')
    create_time = db.Column(db.DateTime, default=db.func.now(), comment='创建时间')
    update_time = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now(), comment='更新时间')
    is_deleted = db.Column(db.Integer, default=0, comment='是否删除')
