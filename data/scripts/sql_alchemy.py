# -*- encoding: utf-8 -*-
"""
@File    :   sql_alchemy.py
@Contact :   zhangjie2@cuhk.edu.cn
@License :   (C)Copyright 2018-2021

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/5/25 15:19   JeasonZhang      1.0         None
"""
from sqlalchemy import create_engine
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/USSchedule?charset=utf8'
engine = create_engine(SQLALCHEMY_DATABASE_URI)
connection = engine.connect()

