class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if 2 * k > n:
            return False
        
        def increasing(start, length):
            for i in range(start, start + length - 1):
                if nums[i] >= nums[i + 1]:
                    return False
            return True

        for n in range(n - 2*k + 1):
            if increasing(n, k) and increasing(n + k, k):
                return True
        return False