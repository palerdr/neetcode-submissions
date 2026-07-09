import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-x for x in nums]
        heapq.heapify(max_heap)

        for i in range(1,k):
            heapq.heappop(max_heap)
        
        ret = -heapq.heappop(max_heap)
        return ret