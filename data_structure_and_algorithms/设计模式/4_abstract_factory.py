"""抽象工厂"""
from abc import ABCMeta, abstractmethod


class PhoneFactory(metaclass=ABCMeta):
    """基础工厂"""

    @abstractmethod
    def make_shell(self):
        pass

    @abstractmethod
    def make_cpu(self):
        pass

    @abstractmethod
    def make_os(self):
        pass


"""具体工厂"""


class MiFactory(PhoneFactory):
    # 小米厂家
    def make_cpu(self):
        return SnapDragonCPU()

    def make_os(self):
        return Android()

    def make_shell(self):
        return BigShell()


class HuaweiFactory(PhoneFactory):
    # 华为厂家
    def make_cpu(self):
        return MediaTekCPU()

    def make_os(self):
        return Android()

    def make_shell(self):
        return SmallShell()


class IPhoneFactory(PhoneFactory):
    # 苹果厂家
    def make_cpu(self):
        return AppleCPU()

    def make_os(self):
        return IOS()

    def make_shell(self):
        return AppleShell()


"""基础产品原型"""


class PhoneShell(metaclass=ABCMeta):

    @abstractmethod
    def show_shell(self):
        pass


class CPU(metaclass=ABCMeta):
    @abstractmethod
    def show_cpu(self):
        pass


class OS(metaclass=ABCMeta):
    @abstractmethod
    def show_os(self):
        pass


"""具体产品"""


class SmallShell(PhoneShell):
    def show_shell(self):
        print("普通小手机壳")


class BigShell(PhoneShell):
    def show_shell(self):
        print("普通大手机壳")


class AppleShell(PhoneShell):
    def show_shell(self):
        print("苹果手机壳")


class SnapDragonCPU(CPU):
    def show_cpu(self):
        print("骁龙CPU")


class MediaTekCPU(CPU):
    def show_cpu(self):
        print("联发科CPU")


class AppleCPU(CPU):
    def show_cpu(self):
        print("苹果CPU")


class Android(OS):
    def show_os(self):
        print("Android系统")


class IOS(OS):
    def show_os(self):
        print("iOS系统")


if __name__ == '__main__':
    # client

    class Phone:
        def __init__(self, cpu, os, shell):
            self.cpu = cpu
            self.os = os
            self.shell = shell

        def show_info(self):
            self.shell.show_shell()
            self.cpu.show_cpu()
            self.os.show_os()


    def make_phone(factory):
        cpu = factory.make_cpu()
        os = factory.make_os()
        shell = factory.make_shell()
        return Phone(cpu, os, shell)


    p = make_phone(IPhoneFactory())
    p.show_info()
