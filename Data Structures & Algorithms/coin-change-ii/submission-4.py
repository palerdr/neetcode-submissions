class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp= [[0]*(len(coins)+1) for _ in range(amount+1)]
        #add 0s on edge cases because there is no way to make amount then
        for i in range(len(coins)):
            dp[0][i] = 1
        #there is only 1 way to make 0 so fill up this row

        for i in range(1,amount+1):
            #skip the 0th row of the table
            for j in range(len(coins)-1,-1,-1):
                #recurrence is dp[i][j] = dp[i][j+1] + dp[i-coin][j]
                dp[i][j] = dp[i][j+1]
                coin = coins[j]

                if amount-coin >= 0:
                    dp[i][j] += dp[i-coin][j] 

        
        return dp[amount][0]
