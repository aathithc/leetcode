class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        mostFreq = 0
        f = 0
        for i in range(len(s)):
            count[s[i]] = 1 + count.get(s[i], 0)
            while (i - f + 1) - max(count.values()) > k:
                count[s[f]] -= 1
                f += 1
            res = max(res, i - f + 1)
        return res




