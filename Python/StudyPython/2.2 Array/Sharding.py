# coding=utf-8

"""
与使用索引来访问单个元素类似，可以使用分片操作类访问一定范围内的元素。
分片的通过冒号隔开的两个索引来实现
"""
tag = '<a href="http://www.python.org">Python web site</a>'
print tag[9:30]
print tag[32:-4]

u"""
分片操作对于提取序列的一部分是很有用的。而编号在这里显得尤为重要。
第1个索引是要提取的第1个元素的编号，而最后的索引则是在分片之后剩余部分的第1个元素的编号。请参见如下代码：
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print numbers[3:6]
print numbers[0:1]