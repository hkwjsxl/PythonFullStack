"""用欧几里得算法实现⼀个分数类，支持分数的四则运算。"""


class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        # 简化a,b，约去最小公倍数
        x = self.gcd(a, b)
        self.a /= x
        self.b /= x

    def gcd(self, a, b):
        """最大公约数"""
        while b > 0:
            tmp = a % b
            a = b
            b = tmp
        return a

    def greatest_common_divisor(self, a, b):
        """
        最小公倍数
        例子：12 16 -> 4 --> 3*4*4=48（init中已经简化了a,b）
        """
        x = self.gcd(a, b)
        return a * b / x

    def __add__(self, other):
        """加法"""
        a = self.a
        b = self.b
        c = other.a
        d = other.b
        # 分母通分
        denominator = self.greatest_common_divisor(b, d)
        # 分子
        numerator = a * denominator / b + c * denominator / d

        return Fraction(numerator, denominator)

    def __sub__(self, other):
        """减法"""
        a = self.a
        b = self.b
        c = other.a
        d = other.b
        # 分母通分
        denominator = self.greatest_common_divisor(b, d)
        # 分子
        numerator = a * denominator / b - c * denominator / d
        return Fraction(numerator, denominator)

    def __mul__(self, other):
        """乘法"""
        a = self.a
        b = self.b
        c = other.a
        d = other.b
        # 分母
        denominator = b * d
        # 分子
        numerator = a * c
        return Fraction(numerator, denominator)

    def __truediv__(self, other):
        """除法(不是整除)"""
        a = self.a
        b = self.b
        c = other.a
        d = other.b
        # 分子分母颠倒
        c, d = d, c
        # 分母
        denominator = b * d
        # 分子
        numerator = a * c
        return Fraction(numerator, denominator)

    def __str__(self):
        return "%d/%d" % (self.a, self.b)


if __name__ == '__main__':
    a = Fraction(1, 3)
    b = Fraction(1, 2)
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
