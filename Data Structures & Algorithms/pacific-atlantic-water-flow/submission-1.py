class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        
        seen = set()
        pacific = set()
        atlantic = set()

        def dfs(x,y,s):
            if not (-1<x<n and -1<y<m):
                return
            s.add((x,y))
            for n1,n2 in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                if not (-1<n1<n and -1<n2<m):
                    continue
                if ((n1,n2)) not in s and heights[n1][n2] >= heights[x][y]:
                    dfs(n1,n2,s)

            
                
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    dfs(i,j,pacific)
                if i == n-1 or j == m-1:
                    dfs(i,j,atlantic)

        return list(pacific.intersection(atlantic))
                