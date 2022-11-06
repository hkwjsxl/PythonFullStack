def num():
    return [lambda x: i * x for i in range(4)]


result = [m(2) for m in num()]
print(result)

# [6,6,6,6]

