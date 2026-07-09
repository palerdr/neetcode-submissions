class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        seen = set()

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
            if board[i][0] == "O":
                dfs(i,0)
        for i in range(n):
            if board[i][m-1] == "O":
                dfs(i,m-1)

        for i in range(m):
            if board[0][i] == "O":
                dfs(0,i)
        for i in range(m):
            if board[n-1][i] == "O":
                dfs(n-1,i)
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "!":
                    board[i][j] = "O"
            
            
