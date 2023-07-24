"""接口"""

from abc import ABCMeta, abstractmethod

"""实现方式一：继承"""


class A:
    def func(self):
        raise NotImplementedError


class B(A):
    def func(self):
        pass


class C(A):
    def func(self):
        pass


"""实现方式二：abc"""


class E(metaclass=ABCMeta):
    @abstractmethod
    def func(self):
        pass


class F(E):
    def func(self):
        pass


class G(E):
    def func(self):
        pass
