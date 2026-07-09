class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        r = set()
        l = set()
        cols = [False]*n
        ret = []
        board = [["."]*n for _ in range(n)]

        def dfs(j):
            if j >= n:
                ret.append(["".join(row) for row in board])
                return 

            for i in range(n):
                if cols[i]:
                    continue
                rd = j-i
                ld = j+i
                if rd in r or ld in l:
                    continue

                r.add(rd)
                l.add(ld)
                cols[i] = True
                board[i][j] = "Q"

                dfs(j+1)

                r.remove(rd)
                l.remove(ld)
                cols[i] = False
                board[i][j] = "."
            return 

        dfs(0)
        return ret


                


