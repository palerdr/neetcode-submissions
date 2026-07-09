class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        n = len(s)
        dp = [False]*(n+1)
        dp[n] = True #base case
        lengths = set(map(len, words))

        for i in range(n-1,-1,-1):
            for L in lengths:
                j = i+L
                if j <= n and s[i:j] in words and dp[j]:
                    dp[i] = True
                    break
        #tries every word length possible from every position, 
        #breaks loop for the first success at that index
        return dp[0]
            