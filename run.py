import pymysql
import json
from app import app

conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       password='123456',
                       database='USSchedule',
                       charset='utf8')
cursor = conn.cursor()
sql = 'SELECT * FROM trump_6_final WHERE trump_6_final.Type="Travel"'
cursor.execute(sql)
row = cursor.fetchone()
# print(row)


@app.route('/database/api', methods=["GET", "POST"])
def data():
    return json.dumps(row)


@app.route('/')
def route_map():
    """
    主视图，返回所有视图网址
    """
    # 遍历路由
    # for rule in app.url_map.iter_rules():
    #     print('name={} path={}'.format(rule.endpoint, rule.rule))
    rules_iterator = app.url_map.iter_rules()
    return json.dumps({rule.endpoint: rule.rule for rule in rules_iterator})

