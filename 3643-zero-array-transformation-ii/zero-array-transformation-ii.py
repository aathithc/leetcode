class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def good(target):
            line = [0 for i in range(len(nums) + 1)]

            for start, end, val in queries[:target]:
                line[start] += val
                line[end + 1] -= val
            
            for i in range(1, len(line)):
                line[i] += line[i - 1]
            
            for n in range(len(nums)):
                if line[n] < nums[n]:
                    return False
            return True
        l = 0
        r = len(queries) + 1
        res = -1
        while l < r:
            m = (l + r) // 2
            if good(m):
                res = m
                r = m
            else:
                l = m + 1
        return res if res != -1 else -1