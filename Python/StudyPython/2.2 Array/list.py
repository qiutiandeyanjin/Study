# coding=utf-8

print list('Hello')

x = [1, 1, 1]
x[1] = 2
print x

names = ['Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Earl']
del names[2]
print names

name = list('Perl')
print name
name[2:] = list('ar')
print name
name[1:] = list('ython')
print name

numbers = [1, 5]
numbers[1:1] = [2, 3, 4]
print numbers
numbers[1:4] = []
print numbers
