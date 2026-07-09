class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [[] for _ in range(n+1)]
        dp[0] = [""]

        for i in range(1,n+1):
            #iterate over solutions up to n
            builder = []
            for k in range(i):
                #choose how to split a and b up to i, iterate over the solutions for a and b 
                for a in dp[k]:
                    for b in dp[i-1-k]:
                        s = "(" + a + ")" + b
                        builder.append(s)
            dp[i] = builder
        
        return dp[n]







        