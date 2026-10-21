from collections import deque
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l,r = 0,n-1
        ans = deque([])
        while l <= r:
            if abs(nums[r]) > abs(nums[l]):
                ans.appendleft(nums[r]*nums[r])
                r -= 1
            else:
                ans.appendleft(nums[l]*nums[l])
                l += 1
        return list(ans)
        