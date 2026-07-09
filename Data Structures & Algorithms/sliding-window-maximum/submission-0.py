import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        ret = []
        q = []
        
        for i in range(len(nums)):
            heapq.heappush(q, (-nums[i],i))

            if len(q) >= k:
                while q[0][1] < i-k+1:
                    heapq.heappop(q)
                    
                ret.append(-q[0][0])


        return ret

                

            


    
    