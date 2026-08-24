class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp is going to store the maximum contiguous subarray after index i
        # thus dp[i] = max(dp[i+1] + nums[i], nums[i])
        # we only need 1 prior value to compute this recurrence

        dp_max = nums[-1]
        dp_i = 0

        for num in nums:
            if dp_i < 0:
                dp_i = 0
            dp_i += num
            dp_max = max(dp_i, dp_max)
        
        return dp_max



