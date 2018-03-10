# !/usr/bin/python
# coding=utf-8

"""
Created on 2017-11-21 20:53:01
@author: ken
Project: 转化Unix时间戳为本地时间
"""

import time

for i in range(100):
    timestamp = raw_input("Please enter unix timestamp(enter 'e' to exit): ")
    if timestamp.isdigit():
        new_time = int(timestamp[:10])
        local_time = time.localtime(new_time)
        dt = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
        print dt
    elif timestamp == 'e':
        print "Bye!"
        break
    else:
        print "Enter value is not a digit"
