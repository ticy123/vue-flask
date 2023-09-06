import os
from flask import Flask
from applications.extensions import init_extensions
from applications.configs.config import config
from applications.views import init_views
from flask_cors import CORS


def create_app(config_type = None):
    """创建Flask，并init各种插件"""
    app = Flask(__name__)
    # 处理跨域问题
    CORS(app, resources=r'/*')
    if not config_type:
        config_type = os.getenv('FLASK_CONFIG', 'development')
    app.config.from_object(config[config_type])
    init_extensions(app)
    init_views(app)
    # init_script(app)
    logo()
    return app


def logo():
    print('''
 _____                              _           _         ______ _           _    
|  __ \                    /\      | |         (_)       |  ____| |         | |   
| |__) |__  __ _ _ __     /  \   __| |_ __ ___  _ _ __   | |__  | | __ _ ___| | __
|  ___/ _ \/ _` | '__|   / /\ \ / _` | '_ ` _ \| | '_ \  |  __| | |/ _` / __| |/ /
| |  |  __/ (_| | |     / ____ \ (_| | | | | | | | | | | | |    | | (_| \__ \   < 
|_|   \___|\__,_|_|    /_/    \_\__,_|_| |_| |_|_|_| |_| |_|    |_|\__,_|___/_|\_\\

    ''')
