# coding=utf-8

# 定义一个数组
data = []
# 让用户输入10个数字
for i in range(10):
    num = input(u"请输入第" + (i + 1) + " 个数字: ")
    data.append(num)

for j in range(len(data) - 1):
    for k in range(len(data) - 1 -j):
        if data[k + 1] > data[k]:
            temp = data[k + 1]
            data[k + 1] = data[k]
            data[k] = temp
            changed = True
    print u"第 %d 次的结果：" % (j + 1)

    for g in data:
        print data[g]