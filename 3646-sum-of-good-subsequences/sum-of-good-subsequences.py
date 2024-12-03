class Solution:
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:
        dp = collections.defaultdict(lambda : [0, 0])
        res = 0
        MOD = 10 ** 9 + 7
        for num in nums:
            count1, all_sum1 = dp[num - 1]
            count2, all_sum2 = dp[num + 1]
            count = count1 + count2 + 1
            all_sum = all_sum1 + all_sum2 + count * num
            dp[num][0] += count
            dp[num][1] += all_sum
            res += all_sum
            res = res % MOD
        return res    