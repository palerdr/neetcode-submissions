class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)

        dp = [[None]*(m+1) for _ in range(n+1)]
  
        def dfs(i, j):
            if dp[i][j] is not None:
                return dp[i][j]

            #base case must match entire string
            if j == m:
                dp[i][j] = (i==n)
                return dp[i][j]
            
            first = i < n and (s[i] == p[j] or p[j] == '.')
            if j+1 < m and p[j+1] == '*': #if in bounds and is star explore both branches
                second = dfs(i, j+2) #skip entirely
                third = first and dfs(i+1, j) #if we match can take 
                res = second or third
            else:
                res = first and dfs(i+1, j+1)
            
            dp[i][j] = res
            return res

        return dfs(0,0)
                
            
            
