#!/usr/bin/env python
#encoding: utf-8
import unittest

__author__ = 'song'


def my_sum(x, y):
    return x + y


def sub(x, y):
    return x - y


class MyTest(unittest.TestCase):
    ##初始化工作
    def setUp(self):
        pass

    #退出清理工作
    def tearDown(self):
        pass

    #具体的测试用例，一定要以test开头
    def test_sum(self):
        self.assertEqual(my_sum(1, 2), 3, 'test sum fail')

    def test_sub(self):
        self.assertEqual(sub(2, 1), 1, 'test sub fail')