# coding=utf-8

# 检查用户名和PIN码

database = [
    ['albert', '1234'],
    ['dilber', '4242'],
    ['smith', '7524'],
    ['jones', '9843']
]
username = raw_input('User name: ')
pin = raw_input('PIN code: ')

if [username, pin] in database:
    print 'Access granted'
else:
    print 'Access Failed'
