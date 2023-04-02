# -*- encoding: utf-8 -*-
"""
@File    :   __init__.py.py
@Contact :   zhangjie2@cuhk.edu.cn
@License :   (C)Copyright 2018-2021

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/3/31 5:41   JeasonZhang      1.0         None
"""

from app.create_app import create_app, DefaultConfig
from flask_sqlalchemy import SQLAlchemy

app = create_app(DefaultConfig)
db = SQLAlchemy(app)
from app.converters.converters import PhoneNumberConverter
app.url_map.converters['phone'] = PhoneNumberConverter

from app.models import model
from app.views import views
