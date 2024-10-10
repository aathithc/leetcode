class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nummap = {}

        for i,n in enumerate(numbers):

            diff = target - n

            if diff in nummap:
                return [nummap[diff]+1, i+1]
            else:
                nummap[n] = i        