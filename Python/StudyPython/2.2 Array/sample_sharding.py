# coding=utf-8

# 对http://www.something.com形式的URL进行分割

url = raw_input('Please enter the URL: ')
domain = url[11:-4]

print "Domain name:" + domain

print [1, 2, 3] + [4, 5, 6]
print 'Hello. ' + 'world'
print [1, 2, 3] + 'world'