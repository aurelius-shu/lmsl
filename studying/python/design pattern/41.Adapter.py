#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
适配模式
'''

from abc import ABCMeta, abstractclassmethod


class Payment(metaclass=ABCMeta):
    @abstractclassmethod
    def pay(self, money):
        pass


class AliPay(Payment):
    def pay(self, money):
        print('AliPay:￥%s' % money)


# 待适配类
class WechatPay(object):
    def fuqian(self, money):
        print('微信支付：￥%s' % money)


# 类适配器
class RealWechatPay(Payment, WechatPay):
    def pay(self, money):
        self.fuqian(money)


# 对象适配器
class AdapterPay(Payment):
    def __init__(self, payment):
        self._payment = payment

    def pay(self, money):
        return self._payment.fuqian(money)


if __name__ == '__main__':
    # 类适配
    AliPay().pay(23)
    RealWechatPay().pay(24)

    # 对象适配
    AliPay().pay(23)
    AdapterPay(WechatPay()).pay(24)
