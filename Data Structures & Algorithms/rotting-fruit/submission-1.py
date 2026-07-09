class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        q = collections.deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((0,i,j))

        time_to_rot = 0
        #diagonal fruits cannot be rotted
        while q:
            l,c1,c2 = q.popleft()
            if l > time_to_rot:
                time_to_rot = l

            for n1,n2 in ((c1+1,c2),(c1-1,c2),(c1,c2+1),(c1,c2-1)):
                if not (-1<n1<n and -1<n2<m):
                    continue
                if grid[n1][n2] == 1:
                    grid[n1][n2] = 2
                    q.append((l+1,n1,n2))
           
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    time_to_rot = -1
                
        return time_to_rot 