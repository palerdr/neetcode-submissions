class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        g = obstacleGrid
        m = len(g)
        n = len(g[0])


        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if g[i][j] == 1:
                    g[i][j] = 0
                elif i == m-1 and j == n-1:
                    g[i][j] = 1
                else:
                    if i+1 >= m:
                        g[i][j] = g[i][j+1]
                    elif j+1 >= n:
                        g[i][j] = g[i+1][j]
                    else:
                        g[i][j] = g[i][j+1] + g[i+1][j]
        return g[0][0]



        