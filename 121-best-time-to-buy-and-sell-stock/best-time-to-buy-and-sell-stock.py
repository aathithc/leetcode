class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        low = prices[0]
        maxp = 0
        for price in prices:
            if price < low:
                low = price
            maxp = max(maxp, price - low)

        return maxp
