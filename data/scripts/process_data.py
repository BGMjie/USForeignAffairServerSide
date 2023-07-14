# -*- encoding: utf-8 -*-
"""
@File    :   process_data.py   
@Contact :   zhangjie2@cuhk.edu.cn
@License :   (C)Copyright 2018-2023
 
@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2023/6/4 23:47   JeasonZhang      1.0         None
"""
import time
from time import struct_time
from typing import List

import pandas as pd
from pandas import DataFrame


"""
    常见日期格式：
    %Y  Year with century as a decimal number.
    %m  Month as a decimal number [01,12].
    %d  Day of the month as a decimal number [01,31].
    %H  Hour (24-hour clock) as a decimal number [00,23].
    %M  Minute as a decimal number [00,59].
    %S  Second as a decimal number [00,61].
    %z  Time zone offset from UTC.
    
    %a  Locale's abbreviated weekday name.
    %A  Locale's full weekday name.
    
    %b  Locale's abbreviated month name.
    %B  Locale's full month name.
    
    %c  Locale's appropriate date and time representation.
    
    %I  Hour (12-hour clock) as a decimal number [01,12].
    
    %p  Locale's equivalent of either AM or PM.
"""


def process_date(before_date: str, format_before: str, format_after: str) -> str:
    """
    此函数对日期按照传入的格式（format_after）对日期进行处理
    :param before_date: 修改前的日期
    :type before_date: str
    :param format_before: 修改前日期的格式
    :type format_before: str
    :param format_after:修改后日期的格式
    :type format_after: str
    :return: 返回格式化后的日期
    :rtype: str
    """
    struct_date: struct_time = time.strptime(before_date, format_before)
    after_date = time.strftime(format_after, struct_date)
    return after_date


def replace_dataframe_date(df: DataFrame, columns: list, format_before: str, format_after: str) -> DataFrame:
    """
    此函数用来对传入的dataframe中的时间列进行替换
    :param df: 传入的DataFrame
    :type df: DataFrame
    :param columns: 对要进行操作的列的名称列表
    :type columns: list
    :param format_before: 修改前日期的格式
    :type format_before: str
    :param format_after:修改后日期的格式
    :type format_after: str
    :return: 返回操作后的DataFrame
    :rtype: DataFrame
    """
    for column in columns:
        date_series = df[column]
        for index, value in date_series.items():
            if not pd.isnull(value):
                ttt = process_date(value, format_before, format_after)
                df[column].at[index] = ttt
    return df


def replace_dataframe_country_comma(df: DataFrame, country_column_name: str) -> DataFrame:
    country_names: str
    for index, country_names in df[country_column_name].items():
        if country_names is not None:
            country_names = country_names.replace(';', ';;').replace(';;;;', ';;')
            df[country_column_name].at[index] = country_names
    return df


def replace_dataframe_country_names(df: DataFrame, country_column_name: str) -> DataFrame:
    country_table: DataFrame = pd.read_excel('../country_lookup.xlsx')
    country_table = country_table.fillna('')
    old_name_list: List[str] = country_table['old_names'].values.tolist()
    new_name_list: List[str] = country_table['names'].values.tolist()
    name_dict = {}

    for old_name, new_name in zip(old_name_list, new_name_list):
        if old_name is not '':
            name_dict[old_name] = new_name

    for index, country_names in df[country_column_name].items():
        if country_names is not None:
            country_name_list: List[str] = country_names.split(';;')
            country_name_list.pop(0)
            for index2, country_name in enumerate(country_name_list):
                country_name_list[index2] = name_dict[country_name]
            replaced_country_names = ';;'.join(country_name_list)
            df[country_column_name].at[index] = replaced_country_names
    return df


def get_country_set(df: DataFrame, country_column_name: str) -> set:
    """
    此函数用来获取
    :param df: 包含城市的DataFrame
    :type df: DataFrame
    :param country_column_name: 包含城市的列的列名
    :type country_column_name: str
    :return: 城市的集合
    :rtype: set
    """
    country_set = set()  # 集合有去重的功能
    for index, value in df[country_column_name].items():
        if value not in [' ']:
            country_list: List[str] = value.split(';;')
            country_list.pop(0)  # 列表的第一项是空的
            country_set.update(country_list)  # 用列表更新集合中的城市
    return country_set


def main():
    # 读取表格
    foreign_affair_table: DataFrame = pd.read_csv('../Merged_final.csv', low_memory=False)
    # # 更改travel_begin列和travel_end的日期个事
    # foreign_affair_table = replace_dataframe_date(foreign_affair_table, columns=['travel_begin', 'travel_end'], format_before='%Y-%m-%d',
    #                                               format_after='%Y-%m-%d')
    # # 将countries_inv列里的分号格式统一为两个分号
    # foreign_affair_table = replace_dataframe_country_comma(foreign_affair_table, country_column_name='countries_inv')
    # # 用country_lookup.xlsx表的"names"列里的国家名称替换countries_inv列里的国家名称
    # foreign_affair_table = replace_dataframe_country_names(foreign_affair_table, country_column_name='countries_inv')
    #
    # # 上述操作是对原表格进行操作，在这里就可以将表格保存下来
    # foreign_affair_table.to_csv('../Merged_final.csv', index=False)

    # 获取表格设计到的国家列表
    country_set = get_country_set(foreign_affair_table, country_column_name='countries_inv')
    country_name_series = pd.Series(list(country_set), name='country')
    country_name_series.to_csv('../country_name_set.csv', index=False)


if __name__ == '__main__':
    main()
