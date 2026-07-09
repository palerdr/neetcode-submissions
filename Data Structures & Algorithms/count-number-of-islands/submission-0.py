class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        num_islands = 0
        visited = set()

        #cannot go to any neighbors
        def dfs(x,y):
            if not (-1<x<n and -1<y<m):
                return
            
            c = grid[x][y]
            if c == '0' or (x,y) in  visited:
                return

            visited.add((x,y))
            dfs(x+1,y)
            dfs(x,y+1)
            dfs(x-1,y)
            dfs(x,y-1)
            

        for i in range(n):
            for j in range(m):
                if (i,j) not in visited and grid[i][j] != "0":
                    dfs(i,j)
                    num_islands += 1
                    
        return num_islands
                
