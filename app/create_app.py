# -*- encoding: utf-8 -*-
"""
@File    :   create_app.py
@Contact :   zhangjie2@cuhk.edu.cn
@License :   (C)Copyright 2018-2021

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/3/31 4:15   JeasonZhang      1.0         None
"""
from flask import Flask


class DefaultConfig(object):
    """默认配置"""
    pass


class DevelopmentConfig(DefaultConfig):
    DEBUG = True


class ProductionConfig(DefaultConfig):
    DEBUG = False


def create_flask_app():
    app = Flask(__name__)
    # print(__name__)
    # 从环境变量指向的配置文件中读取配置信息
    app.config.from_envvar("PROJECT_SETTING", silent=True)
    # static_url_path='/s', static_folder='static', template_folder='templates'
    return app


def create_app(config):
    app = create_flask_app()
    app.config.from_object(config)  # 加载应用中config类的对象，覆盖掉从配置文件中加载的同名配置
    return app
    # print(app.config.get('SQLALCHEMY_DATABASE_URI'))
