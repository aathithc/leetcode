class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        charset = set()

        for i in range(len(s)):
            while s[i] in charset:
                charset.remove(s[l])
                l += 1
            charset.add(s[i])
            res = max(res, i - l + 1)
        return res