class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        dp = [[-1]*(m+1) for _ in range(n+1)]
        #handles edges
        def dfs(i,j):
            if j == m:
                return 1
            if n-i<m-j or i == n:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            #if we can include, move both
            ways = dfs(i+1,j)
            if s[i] == t[j]:
                ways += dfs(i+1,j+1)
            dp[i][j] = ways
            return ways

        return dfs(0,0)