class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        smallest_window_size = float('inf')
        
        l = 0
        current_sum = 0
        for r, num in enumerate(nums):
            current_sum += num
            while current_sum >= target:
                smallest_window_size = min(smallest_window_size, r-l+1)
                current_sum -= nums[l]
                l += 1
        
        return smallest_window_size if smallest_window_size != float('inf') else 0
            