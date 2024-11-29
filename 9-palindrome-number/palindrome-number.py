class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        # Convert the number to a string
        s = str(x)
        
        # Initialize two pointers
        left, right = 0, len(s) - 1
        
        # Compare characters at the two pointers
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True