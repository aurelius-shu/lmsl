#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
简单工厂模式
'''

from abc import ABCMeta, abstractclassmethod


class Payment(metaclass=ABCMeta):
    @abstractclassmethod
    def pay(self, money):
        pass


class AliPay(Payment):
    def pay(self, money):
        print('aliPay:￥%s' % money)


class AppPay(Payment):
    def __init__(self, enable_yuebao=False):
        self._enable_yuebao = enable_yuebao

    def pay(self, money):
        if self._enable_yuebao:
            print('yuebao Pay:￥%s' % money)
        else:
            print('app Pay: ￥%s' % money)


class PaymentFactory(object):
    def create_payment(self, method):
        if method.lower() == 'alipay':
            return AliPay()
        elif method.lower() == 'yuebao':
            return AppPay(True)
        elif method.lower() == 'apppay':
            return AppPay()
        else:
            raise NameError


if __name__ == '__main__':
    paymentFactory = PaymentFactory()
    alipay = paymentFactory.create_payment('alipay')
    alipay.pay(20)

    apppay = paymentFactory.create_payment('apppay')
    apppay.pay(21)

    yuebao = paymentFactory.create_payment('yuebao')
    yuebao.pay(22)
