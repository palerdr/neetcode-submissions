class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #what is the slowest eating speed where you still finish
        
        l,r = 1, max(piles)
        while l <= r:
            m = (l+r)//2
            total_hours = h
            for pile in piles:
                total_hours -= math.ceil(pile/m)
            if total_hours >= 0:
                #this rate worked but we can go slower
                r = m - 1
            else:
                #this rate did not work, must go faster
                l = m + 1
            
        return l
