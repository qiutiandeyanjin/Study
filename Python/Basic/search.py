# coding=utf-8

"""
FileName: search.py
Author: ken
Date: 2018-03-20
Describe: 二分法示例
"""


def search(sequence, number, lower=0, upper=None):
    if upper is None:
        upper = len(sequence) - 1
    if lower == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return search(sequence, number, middle + 1, upper)
        else:
            return search(sequence, number, lower, middle)


seq = [34, 67, 8, 123, 4, 100, 95]
seq.sort()
print seq

print search(seq, 4)

print map(str, range(10))


def func(x):
    return x.isalnum()


seq = ["foo", "x41", "?!", "***"]
print filter(func, seq)

print [x for x in seq if x.isalnum()]

print filter(lambda x: x.isalnum(), seq)

numbers = [72, 101, 108, 108, 111, 44, 32, 119, 111, 114, 108, 100, 33]
print reduce(lambda x, y: x + y, numbers)
