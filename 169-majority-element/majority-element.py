class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        res, maxcount = 0, 0

        for i in nums:
            count[i] = 1 + count.get(i, 0)

            if count[i] > maxcount:
                res = i
                maxcount += 1
            
        return res