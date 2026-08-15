class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = None
        profit = None
        for price in prices:
            if low is None:
                low = price
            else:
                if price < low:
                    low  = price
            
            if profit is None:
                profit = price - low
            else:
                profit = max(profit, price - low)

        return profit if profit >= 0 else 0

            
