from .init_db import init_db
from .init_log import init_log


def init_extensions(app):
    init_log()
    init_db(app)
