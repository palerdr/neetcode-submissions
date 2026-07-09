class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(x,y,s):
            if (x,y) in s:
                return
            if not (-1<x<n and -1<y<m):
                return
            s.add((x,y))
            for n1,n2 in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                if not (-1<n1<n and -1<n2<m):
                    continue
                if heights[n1][n2] >= heights[x][y]:
                    dfs(n1,n2,s)

                
        for i in range(n):
            dfs(i,0,pacific)
            dfs(i,m-1,atlantic)

        for j in range(m):
            dfs(0,j,pacific)
            dfs(n-1,j,atlantic)
            

        return [[x,y] for (x,y) in pacific & atlantic]
                