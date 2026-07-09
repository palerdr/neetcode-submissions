class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        b1 = 0
        b2 = 0
        h1 = 0
        for i in range(n-1,-1,-1):
            tmp = b1
            b1 = max(b1,-prices[i]+h1)
            h1 = max(prices[i]+b2, h1)
            b2 = tmp
        return b1
            
            

        
