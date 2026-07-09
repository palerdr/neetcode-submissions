class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        n = len(nums)
        if total % 2 != 0:
            return False
        target = total//2
        memo = {}

        
        def dfs(i,r):
            if r == 0:
                return True
            if i == n or r < 0:
                return False
            
            if (i,r) in memo:
                return memo[(i,r)]

            memo[(i,r)] = dfs(i+1,r-nums[i]) or dfs(i+1,r)
            return memo[(i,r)]
            
            
        return dfs(0,target)
            