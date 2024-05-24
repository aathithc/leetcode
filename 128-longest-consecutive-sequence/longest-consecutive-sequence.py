class Solution(object):
    def longestConsecutive(self, nums):
        hashset = set(nums)
        longest = 0

        for n in nums:
            #check if it is start of sequence
            if n - 1 not in hashset:
                length = 0
                while (n + length) in hashset:
                    length +=1
                longest = max(length, longest)
        return longest