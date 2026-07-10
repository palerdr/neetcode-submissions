class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #a rectangle containing block i may have at max heights[i] height
        # + the neighbors if they are taller than block i
        #we care about the first smaller bar on the left or right of block i

        def area(l, r, h):
            return (r-l+1) * heights[h]
        heights.append(-1)
        n = len(heights)
        largest_area = 0
        stack = []
        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                j = stack.pop()
                largest_area = max(largest_area, (area(stack[-1]+1 if stack else 0, i-1, j)))
            stack.append(i)
            
        return largest_area
        
