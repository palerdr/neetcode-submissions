class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles) #minimum possible k, max possible k
        while l < r:
            mid = (l + r) // 2 #find middle
            total_hours = sum(-(-pile // mid) for pile in piles) #ceiling division divides pile count by mid
            #so that counts how many hours it will take 
            if total_hours <= h: #case it clears
                r = mid #mid is fast enough, but try a lower rate
            else: #doesn't clear
                l = mid + 1 #mid didn't clear, so lower bound is 1 above mid
        return l #will be minimum bound
