# coding=utf-8

"""
FileName    : while_demo.py
Author      : ken
Date        : 2018-03-18
Describe    : while loop demo
"""

# x = 1
# while x <= 100:
#     print x
#     x += 1

name = ''
while not name.strip():
    name = raw_input('Please enter your name: ')
print 'Hello, %s!' % name
