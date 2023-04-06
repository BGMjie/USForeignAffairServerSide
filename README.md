# 项目介绍

美国外交事务后台

# 项目安装

```shell
conda create --name USForeignAffairServerSide python==3.6.7
conda install flask==1.0.2
pip install flask_sqlalchemy
pip install flask_restful
```

# 项目配置

首先需要配置以下环境变量

```python
FLASK_APP=run.py
PROJECT_SETTING=setting.py
FLASK_DEBUG=1  # 如果不需要开启则填写0
```

# 项目运行

启动项目

```shell
flask run
```

不同位置的参数都存放在Flask包中request对象的不同属性中


| 属性    | 说明                           | 类型           |
| ------- | ------------------------------ | -------------- |
| data    | 记录请求的数据，并转换为字符串 | \*             |
| form    | 记录请求中的表单数据           | MultiDict      |
| args    | 记录请求中的查询参数           | MultiDict      |
| cookies | 记录请求中的cookie信息         | Dict           |
| headers | 记录请求中的报文头             | EnvironHeaders |
| method  | 记录请求使用的HTTP方法         | GET/POST       |
| url     | 记录请求的URL地址              | string         |
| files   | 记录请求上传的文件             | \*             |
