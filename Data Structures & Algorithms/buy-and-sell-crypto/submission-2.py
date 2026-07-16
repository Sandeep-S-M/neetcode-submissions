class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0 
        min_day = float("inf")
        for price in prices:
            min_day = min(min_day,price)
            max_profit = max(max_profit,price - min_day)
        return max_profit

  


 


