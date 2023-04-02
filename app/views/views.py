# -*- encoding: utf-8 -*-
"""
@File    :   views.py
@Contact :   zhangjie2@cuhk.edu.cn
@License :   (C)Copyright 2018-2021

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/3/31 6:08   JeasonZhang      1.0         None
"""
import json
from flask import request
from app import app


# 参数分类：url中的固定参数获取(使用固定参数转换器)，语法：<变量名>，变量名必须作为函数参数传给视图函数
@app.route('/database/api/<string:version>', methods=["GET", "POST"])
def data(version):
    return version


# 自定义固定参数转换器
@app.route('/phone/<phone:phone_number>', methods=["GET", "POST"])
def get_phone_number(phone_number):
    return phone_number


# 请求参数的获取，Flask的request对象使用
@app.route('/para')
def get_parameters():
    name = request.args.get('name')
    password = request.args.get('password')
    return f'name={name}, password= {password}'


@app.route('/form', methods=["GET", "POST"])
def get_form():
    name = request.form.get('name')
    password = request.form.get('password')

    return f'name={name}, password= {password}'


@app.route('/upload', methods=["GET", "POST"])
def get_pic():
    f_pic = request.files['pic_name']
    f_pic.save(r'C:\Users\jie\Documents\code\WorkCode\python\USForeignAffairServerSide\1.png')
    return 'ok'


@app.route('/route')
def route_map():
    """
    主视图，返回所有视图网址
    """
    # 遍历路由
    # for rule in app.url_map.iter_rules():
    #     print('name={} path={}'.format(rule.endpoint, rule.rule))
    rules_iterator = app.url_map.iter_rules()
    return json.dumps({rule.endpoint: rule.rule for rule in rules_iterator})