from flask import Flask
import pymysql
import json

app = Flask(__name__)
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


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!1'


@app.route('/database/api')
def data():
    return json.dumps(row)


if __name__ == '__main__':
    app.run()
