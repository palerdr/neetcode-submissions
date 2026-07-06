class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        smallest_window_size = float('inf')
        
        l = 0
        for r, num in enumerate(nums):
            while sum(nums[l:r+1]) >= target:
                smallest_window_size = min(smallest_window_size, r-l+1)
                l += 1
        
        return smallest_window_size if smallest_window_size != float('inf') else 0
            