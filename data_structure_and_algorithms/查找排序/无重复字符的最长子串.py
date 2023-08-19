class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        end = 0
        dic = {}
        m = 0
        for each in range(len(s)):
            if s[each] in dic:
                end = max(end, dic[s[each]] + 1)
            dic[s[each]] = each
            m = max(m, each - end + 1)

        return m


print(Solution().lengthOfLongestSubstring("abcabcbb"))
