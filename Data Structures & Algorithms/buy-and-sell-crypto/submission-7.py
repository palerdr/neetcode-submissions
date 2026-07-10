class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lo = prices[0]
        for price in prices:
            if price < lo:
                lo = price
            else:
                max_profit = max(max_profit, price - lo)
        return max_profit
            