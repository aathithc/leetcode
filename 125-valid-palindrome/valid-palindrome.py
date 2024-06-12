class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""
        for c in s:
            if c.isalnum():
                new +=c
        new = new.lower()

        f = 0
        l = len(new)-1

        while l>f:
            if new[f] != new[l]:
                return False
            else:
                f+=1
                l-=1
        return True

