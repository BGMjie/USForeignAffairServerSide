# -*- encoding: utf-8 -*-
"""
@File    :   __init__.py.py
@Contact :   zhangjie2@cuhk.edu.cn
@License :   (C)Copyright 2018-2021

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/4/4 5:40   JeasonZhang      1.0         None
"""
from flask import Blueprint
from flask_restful import Api
from utils.output import output_json
from . import trump


us_bp = Blueprint('user', __name__)
us_api = Api(us_bp, catch_all_404s=True)
us_api.representation('application/json')(output_json)
us_api.add_resource(trump.TrumpResource, '/v1_0/trump', endpoint='trump')
