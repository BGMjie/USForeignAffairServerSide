# -*- encoding: utf-8 -*-
"""
@File    :   default.py
@Contact :   zhangjie2@cuhk.edu.cn
@License :   (C)Copyright 2018-2021

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/4/6 3:24   JeasonZhang      1.0         None
"""


class DefaultConfig(object):
    """默认配置"""
    DEBUG = True
    # flask-sqlalchemy使用的参数
    # SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@localhost:3306/USSchedule?charset=utf8'
    # SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1/toutiao'  # 数据库
    SQLALCHEMY_BINDS = {
        'bj-m1': 'mysql+pymysql://root:Jeason52@47.119.165.65:3990/USSchedule?charset=utf8',
        'bj-s1': 'mysql+pymysql://root:Jeason52@47.119.165.65:3990/USSchedule?charset=utf8',
        'masters': ['bj-m1'],
        'slaves': ['bj-s1'],
        'default': 'bj-m1'
    }

    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 追踪数据的修改信号
    SQLALCHEMY_ECHO = True
    SECRET_KEY = 'fih9fh9eh9gh2'

    # CORS
    # TODO 调试后要修改
    CORS_ORIGINS = '*'

    # RESTFUL API设置
    RESTFUL_JSON = {'ensure_ascii': False}  # 不允许将字典中的中文转换成ASCII码

    # FLASK 中文设置
    JSON_AS_ASCII = False


class DevelopmentConfig(DefaultConfig):
    DEBUG = True


class ProductionConfig(DefaultConfig):
    DEBUG = False
