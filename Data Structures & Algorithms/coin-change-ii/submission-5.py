class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] *(amount+1)
        dp[0] = 1
        #solution for amount 0 is 1, and then we build up to amount

        #recurrence for this amount iteration: dp[amount] = dp[amount-coin] + dp[amount]
        #index then build amount for that index
        for i in range(len(coins)-1,-1,-1):
            for j in range(1,amount+1):
                #check if we can add second half or it's just the same as last index solution
                if coins[i] <= j:
                    dp[j] += dp[j - coins[i]]

        return dp[amount]

        

