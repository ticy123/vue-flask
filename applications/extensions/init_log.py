import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)

def init_log():
    logging.basicConfig(level=logging.DEBUG)
    # log config
    file_handler = RotatingFileHandler('./logs/log', maxBytes=1024 * 1024 * 100, backupCount=10)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    # log format
    formatter = logging.Formatter('%(levelname)s %(asctime)s  %(pathname)s:%(lineno)d %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    #  use global object to write log info
    logging.getLogger().addHandler(file_handler)
    logging.getLogger().addHandler(console_handler)
