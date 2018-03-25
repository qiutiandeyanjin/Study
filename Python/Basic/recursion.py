# coding=utf-8

"""
FileName: recursion.py
Author: ken
Date: 2018-03-20
Describe: 递归示例
"""


# def factorial(n):
#     result = n
#     for i in range(1, n):
#         result *= i
#     return result


# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# print factorial(5)

# def power(x, n):
#     result = 1
#     for i in range(n):
#         result *= x
#     return result

def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)


print power(2, 3)
