text = """id,name,age,phone,job
1,alex,22,13651054608,IT 
2,wusir,23,13304320533,Tearcher
3,老男孩,18,1333235322,IT"""

# 将上述数据处理为如下格式的结果：
#    info = [{'id':'1','name':'alex','age':'22','phone':'13651054608','job':'IT'},.... ..]
# 提示：text的内容是根据 \n 分割（\n表示回车换行）。
# data_list = text.split('\n')
# header_list = data_list[0].split(',')
# info = []
# for index in range(1, len(data_list)):
#     item = {}
#     row = data_list[index]
#     row_list = row.split(',')
#     for i in range(len(row_list)):
#         item[header_list[i]] = row_list[i]
#     info.append(item)
# print(info)

# content = input("请输入内容:") # 用户可能输入 5*9*99.... 或 5* 9 * 10 * 99 或 5 * 9 * 99...
#
# # 补充代码实现
# lst = content.split('*')
# i = 1
# for v in lst:
#     v = int(v.strip())
#     i *= v
# print(i)


"""

1*1
2*1 2*2
3*1 3*2 3*3
4*1 4*2 4*3 4*4
5*1 5*2 5*3 5*4 5*5
6*1 6*2 6*3 6*4 6*5 6*6
7*1 7*2 7*3 7*4 7*5 7*6 7*7
8*1 8*2 8*3 8*4 8*5 8*6 8*7 8*8
9*1 9*2 9*3 9*4 9*5 9*6 9*7 9*8 9*9

"""

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f'{i}*{j}={i * j}', end='  ')
#     print()


# v5 = {11,2,("alex",{"北京","上海"},"eric"),33}
# print(v5)

# print(hash((1,23,)))








