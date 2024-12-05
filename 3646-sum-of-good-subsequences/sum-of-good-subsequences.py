class Solution:
    def sumOfGoodSubsequences(self, nums: List[int]) -> int:
        dp = collections.defaultdict(lambda: [0, 0]) #num -> [count, sum]
        res = 0
        mod = 10 ** 9 + 7

        for n in nums:
            count1, sum1 = dp[n - 1]
            count2, sum2 = dp[n + 1]

            count = count1 + count2 + 1
            total = sum1 + sum2 + n * count

            dp[n][0] += count
            dp[n][1] += total
            res += total
            res = res % mod
        return res