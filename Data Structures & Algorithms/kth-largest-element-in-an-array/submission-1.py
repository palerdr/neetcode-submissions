import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums)-k
        #since problem is k largest here we find the element at index len-k sorted

        def qs(l,r):
            pivot,p = nums[r],l
            for i in range(l,r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = pivot, nums[p]

            if p > k:
                return qs(l,p-1)
            elif k > p :
                return qs(p+1,r)
            else:
                return nums[p]
        
        return qs(0, len(nums)-1)