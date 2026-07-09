class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-1]*3 for _ in range(n+1)] #buying,selling,holding
        
        def dfs(i,j):
            if dp[i][j] != -1:
                return dp[i][j]
            if i >= n:
                return 0
            if i == 0:
                return max(dfs(i+1,0), -prices[i] + dfs(i+1,1))

            if j == 2:
                cooldown = dfs(i+1,0)
                dp[i][j] = cooldown
                return cooldown
            if j == 1:
                holding = max(prices[i] + dfs(i+1,2), dfs(i+1,1)) 
                dp[i][j] = holding
                return holding
            if j == 0:
                can_buy = max(dfs(i+1,0), -prices[i] + dfs(i+1,1))
                dp[i][j] = can_buy
                return can_buy

            return -1
        
        return dfs(0,0)
            
            
     