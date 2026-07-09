import functools
class Solution:

    def rob(self, nums: List[int]) -> int:

        @functools.lru_cache()
        def helper(start):
            if start >= len(nums):
                return 0 #empty no houses to rob
            if start == len(nums) - 1:
                return nums[start] #only one house to rob so rob it
            #rob the first house
            c1 = nums[start] + helper(start + 2)
            #skip this house
            c2 = helper(start + 1)
        
            return max(c1,c2)

        return helper(0)
