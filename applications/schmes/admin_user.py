from marshmallow import fields
from applications.extensions.init_db import ma
from applications.models.admin_user import User


class UserOutSchema(ma.Schema):
    id = fields.Integer()
    username = fields.Str()
    password = fields.Str()
    email = fields.Str()
    phone = fields.Str()
    address = fields.Str()



class UserOutSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

    # 自定义输出字段
    title = fields.String(required=True)
    author = fields.String(required=True)
    published_date = fields.Date(required=True)