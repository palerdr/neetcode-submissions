class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        def profit(buy, sell):
            return sell - buy

        n = len(prices)

        dp = [0] * (n)
        
        # most money I can make is max of most money from buying today or max money from tomorrow

        most = prices[n-1]
        for i in range(n-2, -1, -1):
            price = prices[i]
            next_price = prices[i+1]
            most = max(price, most)

            dp[i] = max(
                profit(price, most),
                dp[i+1],
                profit(price, next_price) + dp[i+1],
            )
        
        return dp[0]

        