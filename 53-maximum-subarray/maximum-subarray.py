class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 0
        res = nums[0]

        for i in nums:
            if cur < 0:
                cur = 0
            cur += i
            res = max(cur, res)
        return res