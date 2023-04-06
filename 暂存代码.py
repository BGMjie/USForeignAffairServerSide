# -*- encoding: utf-8 -*-
"""
@File    :   暂存代码.py
@Contact :   zhangjie2@cuhk.edu.cn
@License :   (C)Copyright 2018-2021

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/4/6 3:37   JeasonZhang      1.0         None
"""
import json

from flask import render_template, redirect, jsonify, request

from utils.converters import PhoneNumberConverter
from run import app

app.url_map.converters['phone'] = PhoneNumberConverter


# conn = pymysql.connect(host='localhost',
#                        port=3306,
#                        user='root',
#                        password='123456',
#                        database='USSchedule',
#                        charset='utf8')
# cursor = conn.cursor()
# sql = 'SELECT * FROM trump_6_final WHERE trump_6_final.Type="Travel"'
# cursor.execute(sql)
# row = cursor.fetchone()
# # print(json.dumps(row))

@app.route('/')
def index():
    """
    主视图，返回所有视图网址
    """

    # 第一种返回响应的方式，可以以元组的格式返回信息，格式为(response：响应, status：状态码, headers：响应头)
    # return '状态码为 666', 666, {'name': 'Python'}

    # 第二种返回响应的方式，构造响应对象，以此设置响应体，状态码，响应头然后返回响应对象
    # resp = make_response('make response测试')
    # resp.headers["name"] = "Python"
    # resp.status = "404 not found"
    # 设置cookie
    # resp.set_cookie('username', 'zhang', max_age=3600)
    # 获取cookie
    # username = request.cookies.get('username')
    # return resp

    return render_template('index.html', name='abc')


@app.route('/redirect')
def redirect_to():
    # 重定向的使用,参数为location
    # 应用场景：当项目文件或url地址出现变化的时候
    return redirect('https://www.baidu.com')


@app.route('/json')
def return_json():
    json_dict = {
        "user_id": 10,
        "user_name": "laowang"
    }
    # 返回json数据的第一种方法，但这种方法返回的响应头中的content-type是text/html
    # json_data = json.dumps(json_dict)  # dumps函数的作用是将字典转换成json字符串
    # return json_data
    # 返回json数据的第二种方法，这种方法返回的响应头中的content-type是application/json
    return jsonify(json_dict)


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
    # for rule in src.url_map.iter_rules():
    #     print('name={} path={}'.format(rule.endpoint, rule.rule))
    rules_iterator = app.url_map.iter_rules()
    return json.dumps({rule.endpoint: rule.rule for rule in rules_iterator})


@app.errorhandler(500)
def internal_server_error(e):
    return '服务器搬家了'


@app.errorhandler(ZeroDivisionError)
def zero_division_error(e):
    return '除数不能为0'


# 在第一次请求之前调用，可以在此方法内部做一些初始化操作
@app.before_first_request
def before_first_request():
    print("before_first_request")


# 在每一次请求之前调用，这时候已经有请求了，可能在这个方法里面做请求的校验
# 如果请求的校验不成功，可以直接在此方法中进行响应，直接return之后那么就不会执行视图函数
@app.before_request
def before_request():
    print("before_request")
    # if 请求不符合条件:
    #     return "laowang"


# 在执行完视图函数之后会调用，并且会把视图函数所生成的响应传入,可以在此方法中对响应做最后一步统一的处理
@app.after_request
def after_request(response):
    print("after_request")
    # response.headers["Content-Type"] = "application/json"
    return response


# 请每一次请求之后都会调用，会接受一个参数，参数是服务器出现的错误信息
@app.teardown_request
def teardown_request(error):
    print("teardown_request")
