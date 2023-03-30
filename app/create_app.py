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


def create_flask_app(config):
    """
    创建Flask应用
    :param config: 配置对象
    :return: Flask应用
    """
    # static_url_path='/s', static_folder='static', template_folder='templates'
    app = Flask(__name__)
    app.config.from_object(config)

    # 从环境变量指向的配置文件中读取的配置信息会覆盖掉从配置对象中加载的同名参数
    app.config.from_envvar("PROJECT_SETTING", silent=True)
    return app


class DefaultConfig(object):
    """默认配置"""
    pass


class DevelopmentConfig(DefaultConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/USSchedule?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
