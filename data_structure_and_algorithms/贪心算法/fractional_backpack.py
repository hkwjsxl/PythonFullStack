"""
背包问题
⼀个⼩偷在某个商店发现有n个商品（假设每个商品都不同，且只有一个），第i个商品价值vi元，重wi千克。
他希望拿⾛的价值尽量⾼，但他的背包最多只能容纳W千克的东⻄。他应该拿⾛哪些商品？
举例：
- 商品1：v1=60 w1=10 （每千克6元）
- 商品2：v2=100 w2=20 （每千克5元）
- 商品3：v3=120 w3=30 （每千克4元）
- 背包容量：W=50
"""


def fractional_backpack(goods, total_capacity):
    """
    :param goods: 商品信息
    :param total_capacity: 背包总容量
    :return:
    """
    total_price = 0
    li = [0 for _ in range(len(goods))]
    for index, (price, weight) in enumerate(goods):
        if total_capacity >= weight:
            total_capacity -= weight
            total_price += price
            li[index] = 1
        else:
            total_price += total_capacity * (price / weight)
            li[index] = total_capacity / weight
            break
    # 返回拿走的商品信息和总共得到的金额
    return li, total_price


if __name__ == '__main__':
    goods = [(60, 10), (100, 20), (120, 30)]
    goods.sort(key=lambda x: x[0] / x[1], reverse=True)
    total_capacity = 50
    li, get_price = fractional_backpack(goods, total_capacity)
    print(li, get_price)
