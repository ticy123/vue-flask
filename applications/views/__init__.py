from applications.views.admin import register_admin_views


def init_views(app):
    register_admin_views(app)


