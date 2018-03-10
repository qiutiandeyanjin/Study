# coding=utf-8
import csv #导入csv包

# 读取本地csv文件
date = csv.reader(open('info.csv', 'r'))

# 循环输入每一行信息
for user in date:
    print(user)