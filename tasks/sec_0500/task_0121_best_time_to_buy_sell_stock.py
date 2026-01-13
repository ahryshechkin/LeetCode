class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxProfit = 0
        minPrice = prices[0]
        for price in prices:
            minPrice = min(minPrice, price)
            maxProfit = max(maxProfit, price - minPrice)
        return maxProfit