class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 0
        maxsub = nums[0]

        for i in nums:
            if cur < 0:
                cur = 0
            cur += i
            maxsub = max(maxsub, cur)
        return maxsub

