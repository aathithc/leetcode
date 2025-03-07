# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n 

        while l <= r:
            mid = int((l+r)/2)
            
            if isBadVersion(mid):
                result = mid
                r = mid - 1
            else:
                l = mid + 1
        return result if result else -1
