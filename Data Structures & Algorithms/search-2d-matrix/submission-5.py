class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0,len(matrix)-1

        while l<=r:
            m = r+l//2
            if matrix[m][-1] < target:
                l=m+1
            elif matrix[m][0] > target:
                r=m-1
            else:
                return target in matrix[m]
        return False
            


