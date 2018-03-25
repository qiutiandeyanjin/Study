# coding=utf-8

"""
FileName: params_ex.py
Author: ken
Date: 2018-03-25
Describe: 练习使用参数
"""


def story(**kwds):
    return 'Once upon a time, there was a' \
           '%(job)s called %(name)s.' % kwds


def power(x, y, *others):
    if others:
        print 'Received redundant parameters:', others
    return pow(x, y)


def interval(start, stop=None, step=1):
    """Imitate range() for step > 0"""
    if stop is None:            # 如果没有为stop提供值
        start, stop = 0, start  # 指定参数
    result = []
    i = start                   # 计算start索引
    while i < stop:             # 直到计算到stop的索引
        result.append(i)        # 将索引添加到result内
        i += step               # 用step (>0) 增加索引i
    return result


if __name__ == "__main__":
    print story(job='king', name='Gumby')
    print story(name='Sir Robin', job='brave knight')
    params = {'job': 'language', 'name': 'Python'}
    print story(**params)
    del params['job']
    print story(job='stroke of genius', **params)

    print power(2, 3)
    print power(3, 2)
    print power(y=3, x=2)
    params = (5,) * 2
    print power(*params)
    print power(3, 3, 'Hello, world')

    print interval(10)
    print interval(1, 5)
    print interval(3, 12, 4)
    print power(*interval(3, 7))
