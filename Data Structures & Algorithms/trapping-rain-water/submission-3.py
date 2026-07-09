class Solution:
    def trap(self, height: List[int]) -> int:
        
        l,r = 0, len(height)-1

        local_l = height[l]
        local_r = height[r]
        trapped_water = 0

        while l <= r:
            if local_l < local_r:
                stored_here = max(0, local_l - height[l])
                local_l = max(local_l, height[l])
                l += 1
            
            else:
                stored_here = max(0, local_r - height[r])
                local_r = max(local_r, height[r])
                r -= 1
            
            trapped_water += stored_here
        

        return trapped_water

