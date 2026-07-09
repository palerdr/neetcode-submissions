class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not s1 and not s2 and not s3:
            return True
        n = len(s1)
        m = len(s2)
        k = len(s3)
        if k != n+m:
            return False
        
        dp = [[None]*(m+1) for _ in range(n+1)]

        def dfs(i, j):
            if dp[i][j] is not None:
                return dp[i][j]
            if i+j == k:
                return True
            
            if -1<i<n and s1[i] == s3[i+j] and dfs(i+1,j):
                dp[i][j] = True
                return True

            if -1<j<m and s2[j] == s3[i+j] and dfs(i,j+1):
                dp[i][j] = True
                return True

            dp[i][j] = False
            return False


        return dfs(0,0)
            


