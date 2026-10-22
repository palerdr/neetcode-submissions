class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        
        dp = [None] * (n+1)
        dp[0] = dp[1] = 1

        def num_trees_rec(n):
            if dp[n]:
                return dp[n]
            
            ans = 0
            for i in range(1,n+1):
                ans += num_trees_rec(i-1) * num_trees_rec(n-i)
            dp[n] = ans
            return ans
    
        return num_trees_rec(n)
