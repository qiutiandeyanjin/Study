#!/usr/bin/python
# coding=utf-8
import unittest
import sys

# 添加测试用例目录
sys.path.append('./testCase')

test_dir = './testCase'

discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(discover)
