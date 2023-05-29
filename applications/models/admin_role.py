from applications.extensions.init_db import db
from applications.models.base_model import BaseModel


class Role(BaseModel):
    __tablename__ = 'roles'
    name = db.Column(db.String(50), unique=True, nullable=False)

