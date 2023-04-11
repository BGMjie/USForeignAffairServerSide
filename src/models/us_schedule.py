# -*- encoding: utf-8 -*-
"""
@File    :   us_schedule.py
@Contact :   zhangjie2@cuhk.edu.cn
@License :   (C)Copyright 2018-2021

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/4/6 9:22   JeasonZhang      1.0         None
"""
from datetime import datetime
from . import db


class TrumpFinal(db.Model):
    """
    川普时期外交访问记录表
    """
    __tablename__ = 'trump_with_geo'

    class STATUS:
        ENABLE = 1
        DISABLE = 0
    id = db.Column(db.Integer, primary_key=True, doc='ID')
    date = db.Column(db.Date, default=datetime.now, doc='日期')
    lastname = db.Column(db.String, doc='外交官的姓')
    text = db.Column(db.String, default='None', doc='外交官出访完整的文本')
    links = db.Column(db.String, default='None', doc='文本里有的链接')
    count = db.Column(db.Integer, default=0, doc='序号')
    rank = db.Column(db.Integer, default=0, doc='外交官的等级')
    type = db.Column(db.String, default=None, doc='本条记录的类别')
    travel_places = db.Column(db.JSON, default=None, doc='出访国家及位置')
    travel_start_date = db.Column(db.Date, default=datetime.now, doc='出访的开始时间')
    travel_end_date = db.Column(db.Date, default=datetime.now, doc='出访的结束时间')
    topics = db.Column(db.String, default=None, doc='本条记录的主题')
    meet_countries = db.Column(db.String, default=None, doc='序号')
    link_content = db.Column(db.String, default=None, doc='序号')
