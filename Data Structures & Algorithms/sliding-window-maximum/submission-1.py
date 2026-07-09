from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ret = []
        d = deque() #contains indexes of the numbers rather than numbers

        l,r = 0,0

        while r < len(nums):
            while d and nums[d[-1]] < nums[r]:
                d.pop()
                #get rid of all smaller elements in q
            d.append(r)

            if l > d[0]:
                d.popleft()
            
            if r+1 >= k:
                ret.append(nums[d[0]])
                l+=1
            r+=1


        return ret