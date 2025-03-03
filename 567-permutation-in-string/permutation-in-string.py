from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1m = defaultdict(int)
        s2m = defaultdict(int)

        for c in s1:
            s1m[c] += 1
        
        for i in range(len(s1)):
            s2m[s2[i]] += 1
        
        if s1m == s2m:
            return True
        
        for i in range(len(s1), len(s2)):
            s2m[s2[i]] += 1
            s2m[s2[i - len(s1)]] -= 1

            if s2m[s2[i - len(s1)]] == 0:
                del s2m[s2[i - len(s1)]]
            if s1m == s2m:
                return True
        return False