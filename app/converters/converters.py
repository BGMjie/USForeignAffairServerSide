# -*- encoding: utf-8 -*-
"""
@File    :   converters.py
@Contact :   zhangjie2@cuhk.edu.cn
@License :   (C)Copyright 2018-2021

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/4/2 22:34   JeasonZhang      1.0         None
"""
from werkzeug.routing import BaseConverter


class PhoneNumberConverter(BaseConverter):
    # 匹配规则
    regex = r'1[3-9]\d{9}'

