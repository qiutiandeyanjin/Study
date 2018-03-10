# coding=utf-8
import os

# 定义文件目录
result_dir = 'D:\\Study\\Python\\Selenium Test\\test_project\\report'

lists = os.listdir(result_dir)

# 重新按时间对目录下的文件进行排序
lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn))

print('最新的文件为：' + lists[-1])
file = os.path.join(result_dir, lists[-1])
print(file)