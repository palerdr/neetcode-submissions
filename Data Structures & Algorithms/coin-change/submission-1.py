class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")]*(amount+1)
        dp[0] = 0 #takes 0 coins to make 0 amount

        for i in range(1, amount+1):
            for coin in coins:
                if i-coin >= 0: #ensures we can take the coin
                    dp[i] = min(dp[i], 1 + dp[i-coin])
                    #solution to the problem at amount i is either itself,
                    #or the amount of taking the coin + subproblem

        return dp[amount] if dp[amount] != float("inf") else -1
        