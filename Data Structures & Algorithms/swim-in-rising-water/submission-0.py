class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        pq = [(grid[0][0],0,0)]
        paths = {}
        paths[(0,0)] = grid[0][0]
        
        while pq:
            ct,cx,cy = heapq.heappop(pq)
            if paths[(cx,cy)] < ct:
                continue
            
            neighbors = ((cx+1,cy),(cx-1,cy),(cx,cy+1),(cx,cy-1))
            for n1, n2 in neighbors:
                if not (-1<n1<n and -1<n2<n):
                    continue
                newtime = max(ct, grid[n1][n2])
                if (n1,n2) not in paths or newtime < paths[(n1,n2)]:
                    paths[(n1,n2)] = newtime
                    heapq.heappush(pq, (newtime,n1,n2)) 

        return paths[(n-1,n-1)]
            



