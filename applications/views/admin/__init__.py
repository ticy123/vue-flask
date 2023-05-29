from flask import Blueprint
from flask_restful import Api
from applications.views.admin.user import User, Users

admin_bp = Blueprint("user", __name__, url_prefix="/admin")


def register_admin_views(app):
    add_user_views()
    app.register_blueprint(admin_bp)


def add_user_views():
    # Path: applications\views\admin\user.py
    admin_api = Api(admin_bp)
    admin_api.add_resource(User, '/user/<int:user_id>')
    #http://localhost:5000/admin/users
    admin_api.add_resource(Users, '/users')





