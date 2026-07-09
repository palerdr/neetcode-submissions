class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        n, m = len(text1), len(text2)
        dp = [0]*(n+1)

        for i in range(m-1,-1,-1):
            prev = 0
            for j in range(n-1,-1,-1):
                tmp = dp[j]
                if text1[j] == text2[i]:
                    dp[j] = prev + 1
                else:
                    dp[j] = max(dp[j], dp[j+1])
                prev = tmp
                
        return dp[0]