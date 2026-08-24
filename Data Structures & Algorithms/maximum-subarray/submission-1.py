class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp is going to store the maximum contiguous subarray after index i
        # thus dp[i] = max(dp[i+1] + nums[i], nums[i])
        # we only need 1 prior value to compute this recurrence

        n = len(nums)
        dp_max = nums[-1]
        dp_i = nums[-1]

        for i in range( n-2, -1, -1):
            dp_i = max( dp_i + nums[i], nums[i] )
            dp_max = max(dp_max, dp_i)

        return dp_max



