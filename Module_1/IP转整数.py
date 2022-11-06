ip = "10.3.9.12"

lst = []
ip_list = ip.split('.')
for i in ip_list:
    item = bin(int(i))[2:].zfill(8)
    print(item)
    lst.append(item)
reverse_data = "".join(lst)[::-1]
result = int(reverse_data, base=2)
print(result)




