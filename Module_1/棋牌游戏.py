import random


def random_poker(poker_list):
    index = random.randint(0, len(poker_list) - 1)
    poker = poker_list[index]
    poker_list.pop(index)
    print(poker)
    return poker


def main():
    result = {}
    user_list = ["alex", "武沛齐", "李路飞"]
    kind_list = ['红桃', '黑桃', '梅花', '方块']
    poker_list = []

    for kind in kind_list:
        for i in range(1, 14):
            poker_list.append((kind, i))
    poker_list.append(('小王', 14))
    poker_list.append(('大王', 15))

    for user in user_list:
        print(user.center(50, '-'))

        poker = random_poker(poker_list)
        num = poker[1]
        if num >= 11:
            num = 0.5
        while True:
            single = input('是否继续要牌A/B>>>').strip()
            single = single.upper()
            if single not in ('A', 'B'):
                print('输入错误！')
                continue
            if single == 'B':
                break
            poker = random_poker(poker_list)
            n = poker[1]
            if n >= 11:
                n = 0.5
            num += n
            if num > 11:
                print(f'{user} 爆了，下一个！')
                num = 0
                break
        print(f'{user}分数为：{num}')
        result[user] = num
    print(f'剩余牌数{len(poker_list)}')
    print(result)


if __name__ == '__main__':
    main()
