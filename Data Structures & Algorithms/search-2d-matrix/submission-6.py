class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0,len(matrix)-1

        while l<=r:
            m = (r+l)//2
            if matrix[m][-1] < target:
                l=m+1
            elif matrix[m][0] > target:
                r=m-1
            else:
                sl,sr = 0,len(matrix[m])-1
                while sl <= sr:
                    sm = (sl+sr)//2
                    if matrix[m][sm] < target:
                        sl = sm+1
                    elif matrix[m][sm] > target:
                        sr = sm-1
                    else:
                        return True
                return False
        return False
            


