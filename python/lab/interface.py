

from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        raise NotImplementedError()


class AliPay(Payment):
    def pay(self, money):
        print('pay: ￥%s' % money)



alipay = AliPay()
alipay.pay(100)