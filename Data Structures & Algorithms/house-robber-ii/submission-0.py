import functools
class Solution:
    def rob(self, nums: List[int]) -> int:
        robbed_first = False

        @functools.lru_cache()
        def helper(start, robbed_first):
            if start >= len(nums):
                return 0

            if start == len(nums)-1:
                if not robbed_first:
                    return nums[start]
                else:
                    return 0
            
            if start == 0:
                robbed_first = True
                c1 = nums[start] + helper(start + 2, robbed_first)
                robbed_first = False
                c2 = helper(start + 1, robbed_first)
            else:
                c1 = nums[start] + helper(start + 2, robbed_first)
                c2 = helper(start + 1, robbed_first)

            return max(c1, c2)
        
        return helper(0, robbed_first)