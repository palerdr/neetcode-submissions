class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        INF = 10**18
        max_sum = -INF
        pre_max_sum = -INF
        for num in nums:
            pre_max_sum = max(pre_max_sum + num, num)

            max_sum = max(max_sum, pre_max_sum)
        
        return max_sum
