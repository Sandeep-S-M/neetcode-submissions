class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_day = float("inf")
        for i in range(len(prices)):
            max_profit = max(max_profit,prices[i] - min_day)
            min_day = min(min_day,prices[i])
        return max_profit