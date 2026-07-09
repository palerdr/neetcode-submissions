class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])

        def dfs(x,y):
            if not (-1<x<n and -1<y<m):
                return
            if board[x][y] == "!" or board[x][y] == "X":
                return

            if board[x][y] == "O":
                board[x][y] = "!"

            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)

            return 
        
        for i in range(n):
            for j in range(m):
                if i == 0 or i == n-1 or j == 0 or j == m-1:
                    dfs(i,j)
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "!":
                    board[i][j] = "O"
            
            
