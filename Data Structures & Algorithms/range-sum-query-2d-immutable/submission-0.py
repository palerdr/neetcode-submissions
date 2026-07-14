class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n,m = len(matrix),len(matrix[0])
        self.matrix = matrix
        self.prefixes = [[0] * (m+1) for _ in range(n+1)]
        #pad the top and bottom with zeroes
        #inclusion-exclusion principle
        for i in range(1, n+1):
            for j in range(1, m+1):
                self.prefixes[i][j] = (matrix[i-1][j-1] +
                                        self.prefixes[i-1][j] + #+A
                                        self.prefixes[i][j-1] - #+B
                                        self.prefixes[i-1][j-1]) #-(A&B)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.prefixes[row2 + 1][col2 + 1]
            - self.prefixes[row1][col2 + 1]
            - self.prefixes[row2 + 1][col1]
            + self.prefixes[row1][col1]
        )
