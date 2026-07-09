class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        num_islands = 0
        #visited = set() can mark in plcae rather than visited set but doesn't change space complexity

        #cannot go to any neighbors
        def dfs(x,y):
            if not (-1<x<n and -1<y<m):
                return
            
            c = grid[x][y]
            if c == '0':
                return

            grid[x][y] = '0'
            dfs(x+1,y)
            dfs(x,y+1)
            dfs(x-1,y)
            dfs(x,y-1)
            

        for i in range(n):
            for j in range(m):
                if grid[i][j] != "0":
                    dfs(i,j)
                    num_islands += 1
                    
        return num_islands
                
