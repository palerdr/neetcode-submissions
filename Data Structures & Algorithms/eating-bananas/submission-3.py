class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        #upper bound is the largest pile

        l,r = 1, max(piles)

        while l<r:
            m = (l+r)//2
            totalh = 0
            for pile in piles:
                totalh += math.ceil(pile/m)

            
            
            if totalh > h:
                l = m+1
            else:
                r = m

        return l
            
        
