class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = [[-1]*m for _ in range(n)]

        def dfs(x,y):
            if dp[x][y] != -1:
                return dp[x][y]
            curr = matrix[x][y]
            longest = 1
            for n1,n2 in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                if not(-1<n1<n and -1<n2<m):
                    continue
                if matrix[n1][n2] > curr:
                        longest = max(1+dfs(n1,n2), longest)
            dp[x][y] = longest
            return longest
        
        ret = 0
        for i in range(n):
            for j in range(m):
                    ret = max(ret,dfs(i,j))
        return ret
            


        

