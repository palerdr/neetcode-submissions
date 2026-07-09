class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[-1]*n for _ in range(n)]

        def dfs(l, r):
            if dp[l][r] != -1:
                return dp[l][r]

            if l+1 == r:
                return 0
            
            best = 0
            for i in range(l+1,r):
                score = nums[l]*nums[i]*nums[r]
                best = max(best, dfs(l,i) + dfs(i,r) + score)
                #dfs collapses the intervals so l,i,r are neighbors for score
            dp[l][r] = best
            return best

        return dfs(0,n-1)