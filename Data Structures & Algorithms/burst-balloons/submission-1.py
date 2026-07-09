class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0]*n for _ in range(n)]

        for l in range(n,-1,-1):
            for r in range(l, n):
                best = 0
                for k in range(l+1, r):
                    best = max(best, dp[l][k] + dp[k][r] + nums[l]*nums[k]*nums[r])
                dp[l][r] = best
                
        return dp[0][n-1]
                