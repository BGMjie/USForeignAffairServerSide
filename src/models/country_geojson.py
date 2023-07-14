# -*- encoding: utf-8 -*-
"""
@File    :   country_geojson.py
@Contact :   zhangjie2@cuhk.edu.cn
@License :   (C)Copyright 2018-2021

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/5/5 14:18   JeasonZhang      1.0         None
"""
from datetime import datetime
from . import db


class CountryGeojson(db.Model):
    """
    川普时期外交访问记录表
    """
    __tablename__ = 'country_geojson'

    class STATUS:
        ENABLE = 1
        DISABLE = 0
    id = db.Column(db.Integer, primary_key=True, doc='ID')
    country = db.Column(db.String, default=None, doc='国家名称')
    location = db.Column(db.String, default=None, doc='地理位置')
    geojson = db.Column(db.JSON, default=None, doc='出访国家及位置')
