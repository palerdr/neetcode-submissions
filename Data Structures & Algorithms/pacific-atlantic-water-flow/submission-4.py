class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
    
        pacific = [[False]*m for _ in range(n)]
        atlantic = [[False]*m for _ in range(n)]

        def bfs(starts,ocean):
            q = collections.deque(starts)
            for x,y in starts:
                ocean[x][y] = True

            while q:
                c1,c2 = q.popleft()
                for n1,n2 in ((c1+1,c2),(c1-1,c2),(c1,c2+1),(c1,c2-1)):
                    if not (-1<n1<n and -1<n2<m) or ocean[n1][n2]:
                        continue

                    if heights[c1][c2] <= heights[n1][n2]:
                        ocean[n1][n2] = True
                        q.append((n1,n2))

        pac = [(i,0) for i in range(n)] + [(0,j) for j in range(m)]
        bfs(pac,pacific)
        atl = [(i,m-1) for i in range(n)] + [(n-1,j) for j in range(m)]
        bfs(atl, atlantic)
        return [[x,y] for x in range(n) for y in range(m) if pacific[x][y] and atlantic[x][y]]
            

        