class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        nums = [float('-inf')] + nums
        n = len(nums)

        dp = [[0] * (n+1) for _ in range(n)]

        for j in range(n-1, 0, -1):
            for i in range(0, j):
                keep = 1 + dp[j][j+1]
                skip = dp[i][j+1]
                if nums[i] >= nums[j]:
                    dp[i][j] = skip
                else:
                    dp[i][j] = max(skip, keep)

        return dp[0][1]

                
            
