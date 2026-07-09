class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)

        sub = []

        def dfs(i):
            if i >= len(nums):
                return False
            
            if sum(sub) == total - sum(sub):
                return True

            sub.append(nums[i])
            if dfs(i+1):
                return True
            
            sub.pop()
            if dfs(i+1):
                return True
            
            return False

        return dfs(0)
            