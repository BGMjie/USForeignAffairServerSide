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
from sqlalchemy import and_

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
        req.add_argument('from_date', type=str, required=True, location='args')
        req.add_argument('to_date', type=str, required=True, location='args')
        args = req.parse_args()
        args_from_date = args.from_date
        args_to_date = args.to_date
        print(f'{args_from_date}+{args_to_date}')

        try:
            # 要加载表中的哪些字段
            data_list = TrumpFinal.query.options(load_only(
                TrumpFinal.id,
                TrumpFinal.lastname,
                TrumpFinal.date,
                TrumpFinal.travel_places,

                # User.name,
                # User.profile_photo,
                # User.introduction,
                # User.certificate
            )).filter(and_(TrumpFinal.date.between(args_from_date, args_to_date), TrumpFinal.type == 'Travel')).all()
        except DatabaseError as e:
            current_app.logger.error(e)
            raise e

        # sqlalchemy 中查询数据，如果数据不存在，不会抛出异常报错，而是返回None
        if data_list is not None:
            final_dict = dict()
            for data in data_list:
                print(f'{data.lastname} + {data.date} + {data.travel_places}')
                arr = []
                for place in data.travel_places:
                    place_dit = dict()
                    place_dit['name'] = place
                    place_dit.update(data.travel_places[place])
                    arr.append(place_dit)
                print(place_dit)
                print(type(data.travel_places))
                print(type(data.travel_places[place]))
                arr.append({place: place})
                data_dict = {
                    'lastname': data.lastname,
                    'date': data.date.strftime("%Y-%m-%d"),
                    'travel_places': arr
                }
                final_dict[data.id] = data_dict

            # user_json_str = json.dumps(user_dict)
            # try:
            #     r.setex(self.key, constants.UserProfileCacheTTL.get_val(), user_json_str)
            # except RedisError as e:
            #     current_app.logger.error(e)

            return final_dict
        else:
            # 在sqlalchemy中,如果数据库没有查到数据不会抛出异常报错，而是返回None
            # 返回
            print('没有查询到数据')
            return None
