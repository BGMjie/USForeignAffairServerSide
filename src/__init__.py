# -*- encoding: utf-8 -*-
"""
@File    :   __init__.py.py
@Contact :   zhangjie2@cuhk.edu.cn
@License :   (C)Copyright 2018-2021

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/3/31 5:41   JeasonZhang      1.0         None
"""
from flask import Flask
from flask_cors import CORS


def create_flask_app(config, enable_config_file=False):
    """
    创建Flask应用
    :param config: 配置信息对象
    :param enable_config_file: 是否允许运行环境中的配置文件覆盖已加载的配置信息
    :return: Flask应用
    """
    app = Flask(__name__, static_url_path='/static')
    print(__name__)
    app.config.from_object(config)  # 加载应用中config类的对象，覆盖掉从配置文件中加载的同名配置
    # print('CORS_ORIGINS: ' + app.config.get('CORS_ORIGINS'))
    if enable_config_file:
        from utils import constants
        app.config.from_envvar(constants.GLOBAL_SETTING_ENV_NAME, silent=True)
    # print(src.config.get('SQLALCHEMY_DATABASE_URI'))
    return app


def create_app(config, enable_config_file=False):
    """
    创建应用
    :param config: 配置信息对象
    :param enable_config_file: 是否允许运行环境中的配置文件覆盖已加载的配置信息
    :return: 应用
    """
    app = create_flask_app(config, enable_config_file)
    # 注册url转换器
    from utils.converters import register_converters
    register_converters(app)

    # MySQL数据库连接初始化
    from models import db
    db.init_app(app)
    # print(app)

    # 注册美国外交数据蓝图
    from .Resources.USSchdule import us_bp
    app.register_blueprint(us_bp)

    # 注册跨域
    CORS(app)
    return app
