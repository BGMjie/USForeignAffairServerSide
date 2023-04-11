# -*- encoding: utf-8 -*-
"""
@File    :   trump.py
@Contact :   zhangjie2@cuhk.edu.cn
@License :   (C)Copyright 2018-2021

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/4/6 9:27   JeasonZhang      1.0         None
"""
import json

from flask import current_app
from flask_restful import Resource, reqparse
from flask_restful.inputs import date
# 导入模型类
from models.us_schedule import TrumpFinal
from models import db
from sqlalchemy.orm import load_only
from sqlalchemy.exc import DatabaseError


class TrumpResource(Resource):
    """
    川普信息接口
    """
    def get(self):
        # print(f'总共获取到了{TrumpFinal.query.count()}条数据')
        req = reqparse.RequestParser()
        # req.add_argument('id', type=int, required=True, location='args')
        req.add_argument('date', type=str, required=True, location='args')
        args = req.parse_args()
        # args_id = args.id
        args_date = args.date
        # print(f'{args_id}+{args_date}+{type(args_date)}')

        try:
            # 要加载表中的哪些字段
            data = TrumpFinal.query.options(load_only(
                TrumpFinal.id,
                TrumpFinal.lastname,
                TrumpFinal.date,
                TrumpFinal.travel_places,

                # User.name,
                # User.profile_photo,
                # User.introduction,
                # User.certificate
            )).filter_by(date=args_date).first()
            print(type(data.travel_places))
        except DatabaseError as e:
            current_app.logger.error(e)
            raise e

        # sqlalchemy 中查询数据，如果数据不存在，不会抛出异常报错，而是返回None
        if data is not None:
            # 如果数据库查到数据，形成缓存数据，保存到redis中
            user_dict = {
                'id': data.id,
                'lastname': data.lastname,
                'date': data.date.strftime("%Y-%m-%d"),
                'travel_places': data.travel_places
            }

            # user_json_str = json.dumps(user_dict)
            # try:
            #     r.setex(self.key, constants.UserProfileCacheTTL.get_val(), user_json_str)
            # except RedisError as e:
            #     current_app.logger.error(e)

            return user_dict
        else:
            # 在sqlalchemy中,如果数据库没有查到数据不会抛出异常报错，而是返回None
            # 返回
            print('没有查询到数据')
            return None
