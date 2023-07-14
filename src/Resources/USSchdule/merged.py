# -*- encoding: utf-8 -*-
"""
@File    :   merged.py
@Contact :   zhangjie2@cuhk.edu.cn
@License :   (C)Copyright 2018-2023
 
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2023/6/11 20:01   JeasonZhang      1.0         None
"""
from typing import List

from flask import current_app
from flask_restful import Resource, reqparse
from sqlalchemy import and_

from models.us_schedule import MergeFinal
from models.country_geojson import CountryGeojson
from models import db
from sqlalchemy.orm import load_only
from sqlalchemy.exc import DatabaseError

from geojson import FeatureCollection, Feature


class MergedResource(Resource):
    """
    融合后的
    """
    def get(self):
        req = reqparse.RequestParser()
        req.add_argument('from_date', type=str, required=True, location='args')
        req.add_argument('to_date', type=str, required=True, location='args')
        args = req.parse_args()
        from_date = args.from_date
        to_date = args.to_date
        print(f'{from_date}+{to_date}')

        try:
            # 要加载表中的哪些字段
            data_list: List[MergeFinal] = MergeFinal.query.options(load_only(
                MergeFinal.id,
                MergeFinal.lastname,
                MergeFinal.date,
                MergeFinal.texts,
                MergeFinal.countries_inv,
                MergeFinal.title,
                MergeFinal.travel_begin,
                MergeFinal.travel_end
                # User.name,
                # User.profile_photo,
                # User.introduction,
                # User.certificate
            )).filter(and_(MergeFinal.date.between(from_date, to_date), MergeFinal.travel_type == 1)).all()
        except DatabaseError as e:
            current_app.logger.error(e)
            raise e

        if data_list is not None:
            return_dict = {
                "records": [],
                "countries": set(),
                'gis_data': [],
                'geojson': ''  # 这里的类型应该是FeatureCollection
            }

            for index, data in enumerate(data_list):
                # print(f'{data.id}+{data.lastname}+{data.date}+{data.countries_inv}')
                record = {
                    'key': str(index),
                    "id": data.id,
                    "lastname": data.lastname,
                    "date": data.date.strftime("%Y-%m-%d"),
                    "texts": data.texts,
                    "title": data.title,
                    "travel_begin": data.travel_begin.strftime("%Y-%m-%d"),
                    "travel_end": data.travel_end.strftime("%Y-%m-%d")
                }
                return_dict["records"].append(record)
                countries_inv_list = data.countries_inv.split(';;')
                return_dict["countries"].update(countries_inv_list)
            return_dict["countries"] = list(return_dict["countries"])
            feature_list: List[Feature] = []  # FeatureCollection类需要传入一个Feature数组
            for country in return_dict["countries"]:
                result: CountryGeojson = CountryGeojson.query.options(load_only(
                    CountryGeojson.location,
                    CountryGeojson.geojson
                )).filter(CountryGeojson.country == country).first()
                gis_data = {
                    'name': country,
                    'lng': eval(result.location)[0],
                    'lat': eval(result.location)[1]
                }
                return_dict["gis_data"].append(gis_data)
                feature_list.append(result.geojson)

            country_collection = FeatureCollection(feature_list)  # 构建FeatureCollection对象
            return_dict["geojson"] = country_collection
            return return_dict
        else:
            return {
                "errno": 1,
                "err_msg": "未查询到结果"
            }
