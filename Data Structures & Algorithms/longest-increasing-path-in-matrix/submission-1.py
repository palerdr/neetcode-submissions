class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        q = collections.deque()
        #Multi-source BFS from local maxima
        for i in range(n):
            for j in range(m):
                outdeg = 0
                for c1,c2 in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                    if -1<c1<n and -1<c2<m and matrix[c1][c2] > matrix[i][j]:
                        outdeg += 1
                if outdeg == 0:
                    q.append((i,j))
        
        pl = 0
        while q:
            pl += 1
            for _ in range(len(q)):
                i,j = q.popleft()
                for c1,c2 in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                    if -1<c1<n and -1<c2<m and matrix[c1][c2] < matrix[i][j]:
                        q.append((c1,c2))
        

        return pl


                        
