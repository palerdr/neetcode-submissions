class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        cols = defaultdict(set)
        rows = defaultdict(set)
        cells = defaultdict(set)

        for i, row in enumerate(board):
            for j, entry in enumerate(row):
                #row check going down to ith row
                if entry in rows[i] and entry != "." or row[j] in cols[j] and row[j] != "." or entry in cells[i//3,j//3] and entry != ".":
                    return False
                
                rows[i].add(entry)
                
                cols[j].add(row[j])
                
                cells[i//3,j//3].add(entry)
        return True

        
