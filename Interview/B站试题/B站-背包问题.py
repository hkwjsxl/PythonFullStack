"""
0/1 背包问题
有为N件物品，它们的重量w分别是w1,w2,...,wn，
它们的价值v分别是v1,v2,...,vn，每件物品数量有且仅有一个，
现在给你个承重为M的背包，求背包里装入的物品具有的价值最大总和？
"""


class Solution:
    def fractional_backpack(self, goods, total_capacity):
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


goods = [(60, 10), (100, 20), (120, 30)]
goods.sort(key=lambda x: x[0] / x[1], reverse=True)
total_capacity = 50
li, get_price = Solution().fractional_backpack(goods, total_capacity)
print(li, get_price)
