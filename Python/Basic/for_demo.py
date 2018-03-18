# coding=utf-8

"""
FileName    : for_demo.py
Author      : ken
Date        : 2018-03-18
Describe    : for loop demo
"""

# words = ['this', 'is', 'an', 'ex', 'parrot']
# for word in words:
#     print word
#
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for number in numbers:
#     print number
#
# print range(0, 10)
#
# print range(10)
#
# for number in range(1, 101):
#     print number

# 5.5.3 循环遍历字典元素
# d = {'x': 1, 'y': 2, 'z': 3}
# for key in d:
#     print key, 'corresponds to', d[key]

# 5.5.4 一些迭代工具
# 1. 并行迭代
# names = ['anne', 'beth', 'george', 'damon']
# ages = [12, 45, 32, 102]
# for i in range(len(names)):
#     print names[i], 'is', ages[i], 'years old'
#
# zips = zip(names, ages)
# for name, age in zips:
#     print name, 'is', age, 'years old'
#
# print zip(range(5), xrange(10000000000000))

# 2. 搜索引迭代
# strings = ['xxxxx', 'zzzzzz']
# for string in strings:
#     if 'xxx' in string:
#         index = strings.index(string)
#         strings[index] = '[censored]'
#
# index = 0
# for string in strings:
#     if 'xxx' in string:
#         strings[index] = '[censored]'
#     index += 1
#
# for index, string in enumerate(strings):
#     if 'xxx' in string:
#         strings[index] = '[censored]'
# print strings
#
# print sorted([4, 3, 6, 8, 3])
# print sorted('Hello, world!')
# print list(reversed('Hello, world!'))
# print ''.join(reversed('Hello, world'))

# 跳出循环
# 1.break
# from math import sqrt
# for n in range(99, 0, -1):
#     root = sqrt(n)
#     if root == int(root):
#         print n
#         break

# 2.continue
# for x in seq:
#     if condition1: continue
#     if condition2: continue
#     if condition3: continue
#
#     do_something()

# 3. while True/break习语
# word = 'dummy'
# while word:
#     word = raw_input('Please enter a word: ')
#     # 处理word
#     print 'The word was ' + word

# word = raw_input('Please enter a word: ')
# while word.strip():
#     # 处理word
#     print 'The word was ' + word
#     word = raw_input('Please enter a word: ')

# while True:
#     word = raw_input('Please enter a word: ')
#     if not word:
#         break
#     # 处理word
#     print 'The word was ' + word

# 5.5.6 循环中的else子句
# from math import sqrt
# for n in range(99, 81, -1):
#     root = sqrt(n)
#     if root == int(root):
#         print n
#         break
# else:
#     print "Didn't find it!"

# 5.5.7 列表推导式----轻量级循环
# print [x * x for x in range(10)]
# print [x * x for x in range(10) if x % 3 == 0]
# print [(x, y) for x in range(3) for y in range(3)]
#
# result = []
# for x in range(3):
#     for y in range(3):
#         result.append((x, y))
# print result

girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
# print [b + '+' + g for b in boys for g in girls if b[0] == g[0]]

letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0], []).append(girl)
print [b + '+' + g for b in boys for g in letterGirls[b[0]]]
