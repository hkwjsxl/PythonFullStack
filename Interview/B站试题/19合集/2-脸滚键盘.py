"""
av394281 中，充满威严的蕾米莉亚大小姐因为触犯某条禁忌，被隙间妖怪八云紫（紫m……èi）按住头在键盘上滚动。
同样在弹幕里乱刷梗被紫姐姐做成罪袋的你被指派找到大小姐脸滚键盘打出的一行字中的第 `k` 个仅出现一次的字。
(为简化问题，大小姐没有滚出 ascii 字符集以外的字)

时间限制：C/C++ 1秒，其他语言2秒
空间限制：C/C++ 32M，其他语言64M
输入描述：
    每个输入都有若干行，每行的第一个数字为`k`，表示求第`k`个仅出现一次的字。
    然后间隔一个半角空格，之后直到行尾的所有字符表示大小姐滚出的字符串`S`。
输出描述：
    输出的每一行对应输入的每一行的答案，
    如果无解，输出字符串`Myon~`

(请不要输出多余的空行）

为了方便评测，如果答案存在且为c，请输出[c]
示例1
输入例子：
2 misakamikotodaisuki
3 !bakabaka~ bakabaka~ 1~2~9!
3 3.1415926535897932384626433832795028841971693993751o582097494459211451488946419191919l91919hmmhmmahhhhhhhhhh
7 www.bilibili.com/av170001
1 111
输出例子：
[d]
[9]
[l]
[7]
Myon~
"""

# 题目：打出的一行字中的第 `k` 个仅出现一次的字
import sys

try:
    for line in sys.stdin:
        k, s = line.strip().split(maxsplit=1)
        k = int(k)
        tmp_dict = {}
        tmp_list = []
        for i in range(len(s)):
            current_val = s[i]
            tmp_dict[current_val] = tmp_dict.get(current_val, 0) + 1
        for key, value in tmp_dict.items():
            if value == 1:
                tmp_list.append(key)
        if len(tmp_list) < k:
            print("Myon~")
        else:
            print(f"[{tmp_list[k - 1]}]")
except:
    pass
