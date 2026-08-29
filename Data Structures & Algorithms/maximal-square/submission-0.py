class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix) 
        n = len(matrix[0])

        dp = [[0]*(n) for _ in range(m)]
        # dp[i][j] -> side length of largest square rooted at (i,j)

        maximum = 0
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if matrix[i][j] == '1':
                    if i == m-1 or j == n-1:
                        dp[i][j] = 1
                    else:
                        r,d,dr = dp[i+1][j], dp[i][j+1], dp[i+1][j+1]
                        dp[i][j] = 1 + min(r,d,dr)
                    
                    maximum = max(maximum, dp[i][j])

        
        return maximum ** 2
        