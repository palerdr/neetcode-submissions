class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word2) < len(word1):
            word1,word2 = word2,word1
        n = len(word1)
        m = len(word2)

        INF = 10**18
        
        ndp = [0]*(n+1)
        dp = [n-j for j in range(n+1)]
        #base case out of bounds n-j

        for i in range(m-1,-1,-1): #base case for each is m-ith iteration
            ndp[n] = m-i
            for j in range(n-1,-1,-1):
                if word1[j] == word2[i]:
                    ndp[j] = dp[j+1]
                else:
                    ndp[j] = 1 + min(ndp[j+1],dp[j+1],dp[j])
            dp = ndp[:]
        
        return dp[0]
