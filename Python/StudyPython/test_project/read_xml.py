# coding=utf-8
from xml.dom import minidom

# 打开xml文档
dom = minidom.parse('info.xml')

# 得到文档元素对象
root = dom.documentElement

# print root.nodeName
# print root.nodeValue
# print root.nodeType
# print root.ELEMENT_NODE
# tagname = root.getElementsByTagName('browser')
# print tagname[0].tagName
#
# tagname = root.getElementsByTagName('login')
# print tagname[1].tagName
#
# tagname = root.getElementsByTagName('province')
# print tagname[2].tagName
logins = root.getElementByTagName('login')

# 获取login标签的username属性值
username = logins[0].getAttribute("username")
print username

# 获取login标签的password属性值
password = logins[0].getAttribute("password")
print password

# 获取第二个login标签的username属性值
username = logins[1].getAttribute("username")
print username

# 获取第二个login标签的password属性值
password = logins[1].getAttribute("password")
print password
