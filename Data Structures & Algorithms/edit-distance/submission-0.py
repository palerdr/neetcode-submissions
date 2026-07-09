class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        INF = 10**18
        dp  = [[INF]*(m+1) for _ in range(n+1)]

        def dfs(i,j):
            if dp[i][j] != INF:
                return dp[i][j]

            if not -1<i<n:
                dp[i][j] = m-j
                return m-j

            if not -1<j<m:
                dp[i][j] = n-i
                return n-i
            
            if word1[i] == word2[j]:
                return dfs(i+1,j+1)
            
            rep = 1 + dfs(i+1,j+1)
            ins = 1 + dfs(i,j+1)
            rmv = 1 + dfs(i+1,j)
            ans = min(rep,ins,rmv)
            dp[i][j] = ans
            return ans
        
        return dfs(0,0)
                

        
         