class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #(n-1)x(m-1) board 
        n = len(board) #rows
        m = len(board[0]) #coumns

        #set of coordinate tuples
        def dfs(x,y,i):
            #coordinates and index of the word
            if i == len(word):
                return True
            #base case, bounds check, seen check, recurse on neighbors

            if not (0<=x<n and 0<=y<m):
                return False
            
            if board[x][y] == "TOMB":
                return False

            if board[x][y] != word[i]:
                return False

            tmp = board[x][y]
            board[x][y] = "TOMB"
            if dfs(x+1,y,i+1) or dfs(x-1,y,i+1) or dfs(x,y+1,i+1) or dfs(x,y-1,i+1):
                return True
            board[x][y] = tmp
            
            #backtrack so seen is path independent
            return False

        #dfs for every start in the board
        for i in range(n):
            for j in range(m):
                if dfs(i,j,0):
                    return True

        return False


            

            

            




