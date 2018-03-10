# coding=utf-8

# append
lst = [1, 2, 3]
lst.append(4)
print lst

# count
a = ['to', 'be', 'or', 'not', 'to', 'be']
print a.count('to')

x = [[1, 2], 1, 1, [2, 1, [1, 2]]]
print x.count([1, 2])

# extend
c = [1, 2, 3]
e = [4, 5, 6]
c.extend(e)
print c
c[len(c):] = e
print c

# index
knights = ['We', 'are', 'the', 'knigths', 'who', 'say', 'ni']
print knights.index('who')

# insert
numbers = [1, 2, 3, 5, 6, 7]
numbers.insert(3, 'four')
print numbers

# pop
b = [1, 2, 3]
print b.pop()
print b
print b.pop(0)
print b

# remove
a.remove('be')
print a
# a.remove('bee')
# print a

# reverse
f = [1, 2, 3]
f.reverse()
print f

# sort
g = [4, 6, 2, 1, 7, 9]
h = g[:]
h.sort()
print g
print h

# sorted
i = [4, 6, 2, 1, 7, 9]
j = sorted(i)
print i
print j

print sorted('Python')

# cmp
print cmp(42, 32)
print cmp(99, 100)

k = [5, 2, 9, 7]
k.sort(cmp)
print k

l = ['aardvark', 'abalone', 'acme', 'add', 'aerate']
l.sort(key=len)
print l

m = [4, 6, 2, 1, 7, 9]
m.sort(reverse=True)
print m

# tuple -- 将序列转化为元组
print tuple([1, 2, 3])
print tuple('abc')
print tuple((1, 2, 3))

