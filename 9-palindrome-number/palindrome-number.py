class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        input = x
        new = 0

        while x > 0:
            new = new * 10 + x%10
            x = x//10
        return new == input