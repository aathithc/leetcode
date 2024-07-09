class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        char = set()
        l = 0

        for i in range(len(s)):
            while s[i] in char:
                char.remove(s[l])
                l += 1
            char.add(s[i])
            res = max(res, i - l + 1)
        return res