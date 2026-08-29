class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix) 
        n = len(matrix[0])

        dp = [0]*(n)
        # dp[i][j] -> side length of largest square rooted at (i,j)

        next_dr = 0
        maximum = 0
        for i in range(m-1, -1, -1):
            dr = 0
            for j in range(n-1, -1, -1):
                next_dr = dp[j]
                if matrix[i][j] == '1':
                    if i == m-1 or j == n-1:
                        dp[j] = 1
                    else:
                        r,d = dp[j+1], dp[j]
                        dp[j] = 1 + min(r,d,dr)
                    
                    maximum = max(maximum, dp[j])
                
                else:
                    dp[j] = 0
                
                dr = next_dr
        
        return maximum * maximum
        