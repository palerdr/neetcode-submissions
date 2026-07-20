import bisect
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr) 
        
        idx = bisect.bisect_left(arr, x)

        closest = []
        l,r = idx-1, idx
        # window is exclusive
        while r-l-1 < k:
            if l < 0:
                r += 1
            elif r >= n:
                l -= 1
            else:
                a = arr[l]
                b = arr[r]
                if (abs(a-x) < abs(b-x)) or (abs(a-x)==abs(b-x) and a<b):
                    l -= 1
                else:
                    r += 1

        return arr[l+1:r] 

        
