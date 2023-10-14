# 牛客项目发布项目版本时会有版本号，比如1.02.11，2.14.4等等 现在给你2个版本号version1和version2，请你比较他们的大小 版本号是由
# 修订号组成，修订号与修订号之间由一个"."连接。1个修订号可能有多位数字组成，修订号可能包含前导0，且是合法的。例如，1.02.11，0.1，0.2都是合法的版
# 本号 每个版本号至少包含1个修订号。 修订号从左到右编号，下标从0开始，最左边的修订号下标为0，下一个修订号下标为1，以此类推。 
#  比较规则： 一. 比较版本号时，请按从左到右的顺序依次比较它们的修订号。比较修订号时，只需比较忽略任何前导零后的整数值。比如"0.1"和"0.01"的版本
# 号是相等的 二. 如果版本号没有指定某个下标处的修订号，则该修订号视为0。例如，"1.1"的版本号小于"1.1.1"。因为"1.1"的版本号相当于"1.1.0
# "，第3位修订号的下标为0，小于1 三. version1 > version2 返回1，如果 version1 < version2 返回-1，不然返回0. 
#  数据范围： version1 和 version2 的修订号不会超过int的表达范围，即不超过 32 位整数 的范围 
#  进阶： 空间复杂度 ， 时间复杂度 
#  
#  Related Topics 字符串 双指针 
# 示例:
# 输入:"1.1","2.1"
# 输出:-1 
# 


class BM22compare:
    def compare(self, version1, version2):
        """
        思路：
            split按点分割之后再将长度填充一致，随后分别比较即可
        """
        lst1 = version1.split(".")
        lst2 = version2.split(".")

        # 保证长度一致
        l1 = len(lst1) - 1
        l2 = len(lst2) - 1
        while l1 > l2:
            lst2.append("0")
            l2 += 1
        while l1 < l2:
            lst1.append("0")
            l1 += 1

        i = 0
        while i <= l1:
            if int(lst1[i]) > int(lst2[i]):
                return 1
            elif int(lst1[i]) < int(lst2[i]):
                return -1
            else:
                i += 1
        return 0


print(BM22compare().compare("1.1", "2.1"))
