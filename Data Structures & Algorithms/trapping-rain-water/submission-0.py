class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0 #accumulate water
        l,r = 0, len(height) - 1 #initialize 2 pointers at start and end
        MaxL, MaxR = height[l], height[r] #track max left or right height as you go
        while l < r: 
            if MaxL > MaxR: #if right is less we come in from right
                r -= 1
                MaxR = max(MaxR, height[r]) #update max
                total += MaxR - height[r] #add to total water
            else: 
                l += 1 #if left is less come in from left
                MaxL = max(MaxL, height[l]) 
                total += MaxL - height[l] #is checking current in relation to local max which limits water can be stored
        return total
            
