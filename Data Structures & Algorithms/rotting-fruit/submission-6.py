class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        from collections import deque

        m = len(grid)    
        n = len(grid[0])

        rotten = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rotten.append((i,j))
        
        t = 0
        q = deque(rotten)
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                neighbors = ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))

                for nx, ny in neighbors:
                    if not (-1 < nx < m) or not (-1 < ny < n):
                        continue
                    
                    if grid[nx][ny] == 2 or grid[nx][ny] == 0:
                        continue
                    
                    grid[nx][ny] = 2

                    q.append((nx, ny))
            if q:
                t += 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        
        return t