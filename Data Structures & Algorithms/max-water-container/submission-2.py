class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l,r = 0, len(heights)-1
        most_water = 0

        while l<r:
            current_water = min(heights[l], heights[r]) * (r-l)
            most_water = max(current_water, most_water)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return most_water
