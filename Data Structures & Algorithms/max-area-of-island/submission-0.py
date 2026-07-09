class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        max_area = 0

        def dfs(x,y):
            if not (-1<x<n and -1<y<m):
                return 0 
            if grid[x][y] == 0:
                return 0
            
            grid[x][y] = 0
            return 1 + dfs(x+1,y) + dfs(x,y+1) + dfs(x-1,y) + dfs(x,y-1)

        
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 1:
                    continue

                tmp = dfs(i,j)
                if tmp > max_area:
                    max_area = tmp
                
                
        
        return max_area


        