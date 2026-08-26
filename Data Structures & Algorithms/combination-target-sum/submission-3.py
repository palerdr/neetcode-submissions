class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        n = len(nums)

        r,t = [],[]
        nums.sort()
        
        def dfs(i, s):
            if s == target:
                r.append(t[:])
                return
            if s > target:
                return
            
            for j in range(i, n):
                t.append(nums[j])
                dfs(j, s + nums[j])
                t.pop()

        
        dfs(0, 0)

        return r
            
            
            

        