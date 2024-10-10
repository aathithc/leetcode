class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        f = 0
        for l in range(len(s)):
            count[s[l]] = 1 + count.get(s[l], 0)

            while (l-f+1) - max(count.values()) > k:
                count[s[f]] -= 1
                f += 1
            res = max(res, l-f+1)
        return res