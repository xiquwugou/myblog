#encoding: utf-8
import unittest

__author__ = 'song'


class my_class:
    def __init__(self):
        pass

    def sum(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y


class my_test(unittest.TestCase):

    ##初始化工作
    def setUp(self):
        self.t_class = my_class()   ##实例化了被测试模块中的类

    #退出清理工作
    def tearDown(self):
        pass

    #具体的测试用例，一定要以test开头
    def test_sum(self):
        print '保宗'
        self.assertEqual(self.t_class.sum(1, 2), 3)