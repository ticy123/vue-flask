from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from applications.common.query import Query

db = SQLAlchemy(query_class=Query)
ma = Marshmallow()

def load_model():
    # 必须要load，否则无法创建表和表迁移
    from applications.models import admin_role, admin_user, admin_user_role

def init_table(app):
    db.create_all(app=app)

def init_migration(app):
    Migrate(app, db)

def init_db(app):
    load_model()
    db.init_app(app)
    ma.init_app(app)
    # init_table(app)
    init_migration(app)