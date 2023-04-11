# -*- encoding: utf-8 -*-
"""
@File    :   logger.py
@Contact :   zhangjie2@cuhk.edu.cn
@License :   (C)Copyright 2018-2021

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/2/24 2:09   JeasonZhang      1.0         None
"""
import logging
import time

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s-%(filename)s[lineno:%(lineno)d]-"
                           "%(levelname)s-%(message)s",
                    filemode='log.txt',
                    encoding='utf8',
                    datefmt='%Y-%m-%d %I:%M:%S %p')


def run_time(fun):
    def wrapper():
        start_time = time.time()
        res = fun()
        end_time = time.time()
        print('函数运行时间为%s' % (end_time - start_time))
        return res

    return wrapper
