car_list = ['鲁A32444', '沪B12333', '京B8989M', '京C49678', '黑C46555', '晋B25041', '沪C34567']

# 根据以上代码获取各省车牌数量，例如：info = {"沪":2,"京":2 ...}

# info = {}
# for car in car_list:
#     head = car[0]
#     if not info.get(head):
#         info[head] = 1
#         continue
#     info[head] += 1
# print(info)


# info = {}
# for car in car_list:
#     head = car[0]
#     if head in info:
#         info[head] += 1
#     else:
#         info[head] = 1
# print(info)


info = {}
for car in car_list:
    head = car[0]
    info[head] = info.get(head, 0)
    info[head] += 1
print(info)

