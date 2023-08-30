"""
0/1 背包问题
有为N件物品，它们的重量w分别是w1,w2,...,wn，
它们的价值v分别是v1,v2,...,vn，每件物品数量有且仅有一个，
现在给你个承重为M的背包，求背包里装入的物品具有的价值最大总和？
"""


# class Solution:
#     def fractional_backpack(self, goods, total_capacity):
#         """
#         :param goods: 商品信息
#         :param total_capacity: 背包总容量
#         :return:
#         """
#         total_price = 0
#         li = [0 for _ in range(len(goods))]
#         for index, (price, weight) in enumerate(goods):
#             if total_capacity >= weight:
#                 total_capacity -= weight
#                 total_price += price
#                 li[index] = 1
#             else:
#                 total_price += total_capacity * (price / weight)
#                 li[index] = total_capacity / weight
#                 break
#         # 返回拿走的商品信息和总共得到的金额
#         return li, total_price
#
#
# goods = [(60, 10), (100, 20), (120, 30)]
# goods.sort(key=lambda x: x[0] / x[1], reverse=True)
# total_capacity = 50
# li, get_price = Solution().fractional_backpack(goods, total_capacity)
# print(li, get_price)


def find1array():
    # https://blog.csdn.net/linweieran/article/details/100585052
    C = 10  # 背包总体积
    num = 5  # 物品个数
    v = [4, 3, 5, 2, 5]  # 每个物品体积
    price = [9, 6, 1, 4, 1]  # 初始定义好的价格
    dp = [0 for i in range(C + 1)]  # 定义固定大小()的数组
    for i in range(num):  # 从第i个物品开始遍历
        for j in range(C, v[i] - 1, -1):  # 从容量开始往下递减
            dp[j] = max(dp[j], dp[j - v[i]] + price[i])

    print(dp[C])


find1array()
