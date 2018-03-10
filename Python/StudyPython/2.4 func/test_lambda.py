# coding=utf-8
"""
__Author__: ken
Describe: lambda函数练习
Created on: 2018-01-26
"""


def func(args):
    return args + 1


result = func(123)
print result

my_lambda = lambda args: args + 1

result = my_lambda(123)
print result
