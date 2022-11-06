def fb(n):
    return n if n<2 else fb(n-1)+fb(n-2)

print([fb(n) for n in range(10)])

