# -*- encoding: utf-8 -*-
"""
@File    :   geojson_operate.py
@Contact :   zhangjie2@cuhk.edu.cn
@License :   (C)Copyright 2018-2021

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/4/25 15:11   JeasonZhang      1.0         None
"""
import json
import pandas as pd
from pandas import DataFrame, Series
import geojson
from geojson import FeatureCollection, Feature, MultiPolygon
from geopy import Nominatim, Location
from geopy.exc import GeocoderServiceError

from typing import List, Union


def get_country_location(country_lookup: DataFrame) -> DataFrame:
    geolocator = Nominatim(user_agent="mywebapp", timeout=100)  # , proxies={"http": "192.168.6.207:10809"})
    # location_reverse = geolocator.reverse("15.870032, 100.992541")  # 根据经纬度获取地址
    lng_lat_list = []
    for index, country in country_lookup['names'].items():
        while True:
            try:
                if country == 'The Democratic Republic of the Congo':  # 这里做替换是因为这个刚果民主共和国在{nominatim.openstreetmap.org}中查不到
                    country = 'Congo-Kinshasa'
                location: Union[Location, None] = geolocator.geocode(country)  # 根据地址获取经纬度
                if location:  # 判断返回的是不是None，如果没查到就返回的是None
                    lng_lat = [location.longitude, location.latitude]  # 经纬度列表
                    print(f'{country}:{lng_lat}')
                    lng_lat_list.append(json.dumps(lng_lat))
                else:
                    print(country)
                    lng_lat_list.append(json.dumps([]))
                break
            except GeocoderServiceError as e:
                print(e)
                continue
    country_location = DataFrame()
    country_location['countries'] = country_lookup['names']
    country_location['lng_lat'] = pd.Series(lng_lat_list)
    return country_location


def replace_country_name(origin_filename: str, output_filename: str, country_lookup: DataFrame):
    with open(origin_filename, "r", encoding='utf8') as origin_file:
        line = origin_file.readline()  # 压缩过后的geojson只有一行
        for i in range(len(country_lookup)):
            origin_str = str(country_lookup['name_in_geojson'][i])  # 该列中存的是原始文件中的国家的名称
            replaced_str = str(country_lookup['names'][i])  # 该列中存的是要替换成的国家的名称
            print(origin_str, replaced_str)
            line = line.replace(origin_str, replaced_str)  # 进行替换
        with open(output_filename, 'w+', encoding='utf8') as output_file:
            output_file.write(line)


def open_geojson(filename: str):
    with open(filename, "r", encoding='utf8') as read_content:
        return geojson.load(read_content)


def print_names(feature: Feature):
    print(f"{feature.get('properties').get('NAME_ENG')}\t{feature.get('properties').get('NAME_CHN')}")


def traversal_features(features: List[Feature]):
    """
    # feature_type = feature.get('type')
    #
    # polygons: MultiPolygon = feature.get('geometry')
    # polygons.get('type')
    # print(type(polygons.get('coordinates')))
    #
    # properties: dict = feature.get('properties')
    # properties.get('NAME_CHN')
    # properties.get('NAME_ENG')
    # properties.get('NR_C')
    # properties.get('NR_C_ID')
    # properties.get('SOC')

    # print_names(feature)
    """
    pass


def feature_operation(geojson_filename: str):
    # 打开替换后的geojson文件
    collections: FeatureCollection = open_geojson(geojson_filename)
    # 拿到里面所有的feature，每一个feature是一个国家
    features: List[Feature] = collections.get('features')
    # 遍历所有feature，对每个feature进行操作
    traversal_features(features)


def get_country_feature_map(geojson_filename: str) -> dict:
    collections: FeatureCollection = open_geojson(geojson_filename)
    # 拿到里面所有的feature，每一个feature是一个国家
    features: List[Feature] = collections.get('features')
    # 遍历所有feature，对每个feature进行操作
    # 每一个国家对应一个FeatureCollection，这个FeatureCollection中只有一个Feature
    country_feature_map = {}
    feature: Feature
    for feature in features:
        country_name: str = feature.get('properties').get('NAME_ENG')  # 拿到国家的名称

        # print(str(country_collection))
        country_feature_map[country_name] = feature  # 把国家名称和FeatureCollection对象进行映射
    return country_feature_map


def main():
    """
    该文件主要用来获取country_lookup中names列中国家的location和geojson面数据
    """
    # 1. 读取country_lookup文件
    # country_lookup: DataFrame = pd.read_excel('../country_lookup.xlsx')
    # 2. 获取country_lookup中names列中国家的location，并新建一个表，第一列照搬country_lookup表里的names，改名为countries，第二列是location
    # country_location = get_country_location(country_lookup)
    # country_location.to_csv('../country_location.csv', index=False, header=True)
    # 3. 替换从ant-v网站下下来的原始
    # replace_country_name('../world-antv-compressed.json', '../world-antv-compressed-replaced.json', country_lookup)  # 文件只需要替换一次就行了
    # 4. 获取geojson文件中每个国家的geojson面数据，返回一个字典，格式为{国家名：FeatureCollection}
    country_feature_map = get_country_feature_map("../world-antv-compressed-replaced.json")
    # 把这一步的结果保存起来
    with open('../country_feature_map.json', 'w+', encoding='utf8') as f:
        json.dump(country_feature_map, f)

    # 5. 由于第2步很耗时，所以把第2步的结果保存在country_location.csv，后面只需要读取这个文件就可以了
    country_location = pd.read_csv('../country_location.csv')
    country_location['country_feature_map'] = pd.Series()
    country_location.fillna('', inplace=True)
    for index, country in country_location['countries'].items():
        if country in country_feature_map.keys():
            country_location['country_feature_map'].at[index] = json.dumps(country_feature_map[country])
        else:
            country_location['country_feature_map'].at[index] = {}
    country_location.to_csv('../country_geojson.csv', index=False, header=True)
    # feature_operation(country_lookup, )


if __name__ == '__main__':
    main()
