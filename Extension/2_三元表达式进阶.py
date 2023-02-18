def number(a, b):
    # 如果a>b, re1=a, 否则, re1=b
    re1 = a if a > b else b
    # 如果条件成立, re2=True对应的值a, 反之, re2 =False对应的值
    re2 = {True: a, False: b}[a > b]
    # (不成立的值, 成立的值)[条件]
    re3 = (b, a)[a > b]

    return re1, re2, re3

print(number(10, 20))

