#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
工厂模式
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


class PaymentFactory(metaclass=ABCMeta):
    @abstractclassmethod
    def create_payment(self):
        pass


class AliPaymentFactory(PaymentFactory):
    def create_payment(self):
        return AliPay()


class AppPaymentFactory(PaymentFactory):
    def create_payment(self):
        return AppPay()


class YuebaoPaymentFactory(PaymentFactory):
    def create_payment(self):
        return AppPay(True)


if __name__ == '__main__':
    alipay = AliPaymentFactory().create_payment()
    alipay.pay(20)

    apppay = AppPaymentFactory().create_payment()
    apppay.pay(21)

    yuebao = YuebaoPaymentFactory().create_payment()
    yuebao.pay(22)
