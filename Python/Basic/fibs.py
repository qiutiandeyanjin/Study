# coding=utf-8

"""
FileName    : fibs.py
Author      : ken
Date        : 2018-3-18
Describe    : 抽象
"""


# def fibs(num):
#     fibs01 = [0, 1]
#     for i in range(num - 2):
#         fibs01.append(fibs01[-2] + fibs01[-1])
#     return fibs01
#
#
# num = input('How many numbers do you want? ')
# print fibs(num)

def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}


def lookup(data, label, name):
    return data[label].get(name)


def store(data, *full_names):
    for full_name in full_names:
        names = full_name.split()
        if len(names) == 2:
            names.insert(1, '')
        labels = 'first', 'middle', 'last'
        for label, name in zip(labels, names):
            people = lookup(data, label, name)
            if people:
                people.append(full_name)
            else:
                data[label][name] = [full_name]


d = {}
init(d)
store(d, 'Han Solo')
store(d, 'Luke Skywalker', 'Anakin Skywalker')
print lookup(d, 'last', 'Skywalker')


#
#
# MyNames = {}
# init(MyNames)
# store(MyNames, 'Magnus Lie Hetland')
# print lookup(MyNames, 'middle', 'Lie')
#
# store(MyNames, 'Robin Hood')
# store(MyNames, 'Robin Locksley')
# store(MyNames, 'Mr. Gumby')
# print lookup(MyNames, 'middle', '')
# print MyNames

def inc(x):
    x[0] = x[0] + 1


foo = [11]
inc(foo)
print foo
