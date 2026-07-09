class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if n == 1 and m == 1:
            return 1
        
        dp = [1] * n
        for j in range(n):
            dp[j] = 1
        

        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                dp[j] = dp[j+1] + dp[j]

        return dp[0]
        