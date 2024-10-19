class Solution:
    def firstUniqChar(self, s: str) -> int:
        mp = {}

        for a in s:
            mp[a] = 1 + mp.get(a, 0)
        
        for i in range(len(s)):
            if mp[s[i]] == 1:
                return i
        return -1