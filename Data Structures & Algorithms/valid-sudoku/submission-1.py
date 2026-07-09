class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        cols = defaultdict(set)
        rows = defaultdict(set)
        cells = defaultdict(set)

        for i, row in enumerate(board):
            for j, entry in enumerate(row):
                #row check going down to ith row
                if entry in rows[i] and entry != ".":
                    return False
                else:
                    rows[i].add(entry)
                #column chceck going to jth column
                if row[j] in cols[j] and row[j] != ".":
                    return False
                else:
                    cols[j].add(row[j])
                #cell check for i//3,j//3 cell 
                if entry in cells[i//3,j//3] and entry != ".":
                    return False
                else:
                    cells[i//3,j//3].add(entry)
        return True

        
