class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        pq = collections.deque()
        pacific = [[False]*m for _ in range(n)]
        atlantic = [[False]*m for _ in range(n)]

        def bfs(q,ocean):
            while q:
                c1,c2 = q.popleft()
                for n1,n2 in ((c1+1,c2),(c1-1,c2),(c1,c2+1),(c1,c2-1)):
                    if not (-1<n1<n and -1<n2<m) or ocean[n1][n2]:
                        continue

                    if heights[c1][c2] <= heights[n1][n2]:
                        if ocean[c1][c2]: 
                            ocean[n1][n2] = True
                        q.append((n1,n2))
        for i in range(n):
            pacific[i][0] = True
            pq.append((i,0))
        for j in range(m):
            pacific[0][j] = True
            pq.append((0,j))
        bfs(pq,pacific)

        for i in range(n):
            atlantic[i][m-1] = True
            pq.append((i,m-1))
        for j in range(m):
            atlantic[n-1][j] = True
            pq.append((n-1,j))
        bfs(pq,atlantic)
        return [[x,y] for x in range(n) for y in range(m) if pacific[x][y] and atlantic[x][y]]
            

        