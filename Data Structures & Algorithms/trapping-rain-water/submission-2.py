class Solution:
    def trap(self, height: List[int]) -> int:
        lmax, rmax, trapped = 0,0,0
        l,r = 0, len(height)-1
        while l<r:
            if height[l] < height[r]:
                if height[l] >= lmax:
                    lmax = height[l]
                else:
                    trapped += lmax - height[l]
                l += 1
            else: 
                if height[r] >= rmax:
                    rmax = height[r]
                else:
                    trapped += rmax - height[r]
                r -= 1
    
        return trapped