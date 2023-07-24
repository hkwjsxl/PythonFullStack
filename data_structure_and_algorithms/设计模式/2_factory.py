"""简单工厂模式"""
from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


class Alipay(Payment):
    def pay(self, money):
        print("alipay %d" % money)


class Wechatpay(Payment):
    def pay(self, money):
        print("wechatpay %d" % money)


class PaymentFactory:
    def create_pay_factory(self, method):
        if method == "alipay":
            return Alipay()
        elif method == "wechatpay":
            return Wechatpay()
        else:
            raise ValueError


if __name__ == '__main__':
    pf = PaymentFactory()
    p = pf.create_pay_factory("alipay")
    p.pay(100)
