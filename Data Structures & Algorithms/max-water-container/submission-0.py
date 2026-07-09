class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L,R = 0, len(heights)-1
        Area = 0
        while L < R:
            length = R - L
            height = min(heights[R], heights[L])
            Area = max(Area, height * length)
            if heights[R] > heights[L]:
                L += 1
            elif heights [L] > heights[R]:
                R -= 1
            else:
                R -= 1 
        return Area
        

