class Solution:
    def longestPalindrome(self, s: str) -> int:
        pset = set()
        l = 0

        for i in s:
            if i in pset:
                pset.remove(i)
                l +=2
            else:
                pset.add(i)
        if pset:
            l += 1                

        return l