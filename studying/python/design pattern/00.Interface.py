#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
接口
一种特殊的类，声名若干方法，要求继承该接口的类必须实现这些方法
作用：限制子类的方法名和调用方式，隐藏实现
'''


from abc import ABCMeta, abstractclassmethod


class Payment(metaclass=ABCMeta):
    @abstractclassmethod
    def pay(self, money):
        pass  # raise NotImplementedError


class AliPay(Payment):

    def pay(self, money):
        print('alipay:￥%s' % money)


class AppPay(Payment):

    def pay(self, money):
        print('apppay:￥%s' % money)
