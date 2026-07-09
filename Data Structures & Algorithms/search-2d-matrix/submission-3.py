class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #all in ascending order
        for i,lst in enumerate(matrix):
            if lst[0] <= target <= lst[-1]:
                l,r = 0, len(lst)-1
                while l <= r:
                    m = (l+r)//2
                    if lst[m] > target:
                        r = m-1
                    elif lst[m] < target:
                        l = m+1
                    else:
                        return True
        return False