class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        return sum(max(0, prices[i+1] - prices[i]) for i in range(n-1))
    