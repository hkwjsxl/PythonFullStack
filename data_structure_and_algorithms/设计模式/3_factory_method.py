"""工厂方法模式"""
from abc import ABCMeta, abstractmethod

"""基本模型类"""
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


"""工厂"""
class PaymentFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_payment(self):
        pass


class AlipayFactory(PaymentFactory):
    def create_payment(self):
        return Alipay()


class WechatpayFactory(PaymentFactory):
    def create_payment(self):
        return Wechatpay()


# client
pf = AlipayFactory()
p = pf.create_payment()
p.pay(100)
