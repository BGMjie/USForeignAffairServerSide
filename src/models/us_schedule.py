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


class MergeFinal(db.Model):
    """
    所有总统外交访问记录表
    """
    __tablename__ = 'merge_final'

    class STATUS:
        ENABLE = 1
        DISABLE = 0

    id = db.Column(db.Integer, primary_key=True, doc='ID')
    index_of_each_president = db.Column(db.Integer, default=datetime.now, doc='不同总统下的ID')
    admin = db.Column(db.String, default=None, doc='总统名称')
    date = db.Column(db.Date, default=datetime.now, doc='该条记录的产出日期')
    lastname = db.Column(db.String, default=None, doc='外交官的姓')
    title = db.Column(db.String, default=None, doc='外交官的头衔')
    rank = db.Column(db.Integer, default=None, doc='外交官的等级')
    texts = db.Column(db.String, default=None, doc='该条记录的全部文本')
    links = db.Column(db.String, default=None, doc='该条记录文本中所含有的链接')
    content = db.Column(db.String, default=None, doc='链接中含有的文本')
    counts = db.Column(db.Integer, default=datetime.now, doc='')
    travel_type = db.Column(db.Integer, default=None, doc='出访类型')
    meet_type = db.Column(db.Integer, default=None, doc='会面类型')
    talk_type = db.Column(db.Integer, default=None, doc='谈话类型')
    other_type = db.Column(db.Integer, default=None, doc='其他类型')
    travel_begin = db.Column(db.Date, default=datetime.now, doc='出访的开始时间')
    travel_end = db.Column(db.Date, default=datetime.now, doc='出访的结束时间')
    countries_inv = db.Column(db.String, default=None, doc='涉及的国家')
    accompanies = db.Column(db.String, default=None, doc='和谁一起去的')
    topics = db.Column(db.String, default=None, doc='主题')
    orgs = db.Column(db.String, default=None, doc='涉及的组织')
    presidential = db.Column(db.Integer, default=None, doc='序号')
