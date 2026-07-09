class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word2) < len(word1):
            word1,word2 = word2,word1
        n = len(word1) #shorter word for most optimal space
        m = len(word2)
        dp = [n-j for j in range(n+1)]

        
        for i in range(m-1,-1,-1):
            prev = dp[n]
            dp[n] = m-i
            #base case each time must be set since it's not just 0 it's iteration dependent
            for j in range(n-1,-1,-1):
                tmp = dp[j]
                if word1[j] == word2[i]:
                    dp[j] = prev
                else:
                    dp[j] = 1+min(dp[j], prev, dp[j+1]) #down,diag,right
                prev = tmp #value before overwrite
        return dp[0]