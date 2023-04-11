# -*- encoding: utf-8 -*-
"""
@File    :   __init__.py.py
@Contact :   zhangjie2@cuhk.edu.cn
@License :   (C)Copyright 2018-2021

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/3/31 6:06   JeasonZhang      1.0         None
"""
from .db_routing.routing_sqlalchemy import RoutingSQLAlchemy


db = RoutingSQLAlchemy()
print(db)
