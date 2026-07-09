class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        n = len(s)
        dp = [None]*(n+1)
        #set of all possible word lengths
        lengths = set(map(len, words))

        def dfs(i):
            if i >= n:
                return True
            if dp[i] is not None:
                return dp[i]

            for L in lengths:
                if i + L <= n and s[i:i+L] in words and dfs(i+L):
                    dp[i] = True
                    return True
            
            dp[i] = False
            return False
        
        return dfs(0)
