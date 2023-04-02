# -*- encoding: utf-8 -*-
"""
@File    :   user.py
@Contact :   zhangjie2@cuhk.edu.cn
@License :   (C)Copyright 2018-2021

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/4/3 1:09   JeasonZhang      1.0         None
"""
from flask import Blueprint

user = Blueprint('user', __name__)


@user.route('/users')
def get_users():
    return 'userinfo'
