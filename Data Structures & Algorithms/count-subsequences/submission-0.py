class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        dp = [[-1]*m for _ in range(n)]
        
        def dfs(i,j):
            if not (-1<i<n and -1<j<m):
                return 0
            if n-i < m-j:
                dp[i][j] = 0
            if dp[i][j] != -1:
                return dp[i][j]

            ways = 0
            if s[i] == t[j]:
                if j == len(t)-1:
                    ways += 1
                ways += dfs(i+1,j+1)
            ways += dfs(i+1,j)
            dp[i][j] = ways
            return ways

        return dfs(0,0)


        