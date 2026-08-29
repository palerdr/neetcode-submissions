class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        g = grid
        m = len(g)
        n = len(g[0])


        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                c = g[i][j]
                if i == m-1 and j == n-1:
                    continue
                elif i+1 >= m:
                    g[i][j] = c + g[i][j+1]
                elif j + 1 >= n:
                    g[i][j] = c + g[i+1][j]
                else:
                    g[i][j] = c + min(
                        g[i][j+1],
                        g[i+1][j],
                    )
        return g[0][0]


        