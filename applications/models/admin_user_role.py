from applications.extensions.init_db import db
from applications.models.base_model import BaseModel

class UserRole(BaseModel):
    __tablename__ = 'user_roles'

    user_id = db.Column(db.Integer,nullable=False)
    role_id = db.Column(db.Integer,nullable=False)