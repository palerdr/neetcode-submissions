class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])
        l = 2147483647

        def can_traverse(x,y):
            return -1<x<n and -1<y<m and grid[x][y] != -1

        q = collections.deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i,j))
        
        while q:
            c1,c2 = q.popleft()
            neighbors = [(c1+1,c2),(c1-1,c2),(c1,c2+1),(c1,c2-1)]
            for n1,n2 in neighbors:
                if can_traverse(n1,n2):
                    if grid[n1][n2] == l:
                        grid[n1][n2] = grid[c1][c2]+1
                        q.append((n1,n2))


        return
            

            
