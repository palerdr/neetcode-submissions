class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #checks rows
        r = 0
        for lst in board:
            rlist = []
            rcheck = []
            for s in lst:
                    if s not in rlist or s == '.': #only adds if not duplicate or '.'
                        rlist.append(s)
                    else:
                        rcheck.append(s)
            if rcheck == []: #should be empty if valid
                r += 1 #if rows are valid will be 9 at end
        #checks columns
        c = 0
        for i in range(9):
            clist = []
            ccheck = []
            for lst in board: #adds number at i to column list
                if lst[i] not in clist or lst[i] == '.': 
                    clist.append(lst[i])
                else:
                    ccheck.append(lst[i])
            if ccheck == []:
                c += 1 
        #checks grids
        g = 0
        for block_row in range(0, 9, 3):      
            for block_col in range(0, 9, 3):  
                glist = []
                gcheck = []
                for i in range(3):
                    for j in range(3):
                        cell = board[block_row+i][block_col+j]
                        if cell not in glist or cell == '.':
                            glist.append(cell)
                        else:
                            gcheck.append(cell)
                if gcheck == []:
                        g += 1
        return r == 9 and c == 9 and g == 9
































