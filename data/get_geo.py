# -*- encoding: utf-8 -*-
"""
@File    :   get_geo.py
@Contact :   zhangjie2@cuhk.edu.cn
@License :   (C)Copyright 2018-2021

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/4/9 9:37   JeasonZhang      1.0         None
"""
import json
from geopy.geocoders import Nominatim


def main():
    geolocator = Nominatim(user_agent="mywebapp")
    import pandas as pd
    df = pd.read_csv('place_set.csv', index_col=0)
    from time import sleep
    place_json_list = []
    for place in df['place']:
        location = geolocator.geocode(place)
        obj = dict()
        sleep(1)
        obj[place] = {'latitude': location.latitude, 'longitude': location.longitude}
        place_json_list.append(json.dumps(obj))
    df['place_geo_dict'] = pd.Series(place_json_list)
    df.to_csv('place_geo_dict.csv')


if __name__ == '__main__':
    main()
