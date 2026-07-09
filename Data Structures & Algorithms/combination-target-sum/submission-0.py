class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        cands = []

        def dfs(i, target):
            if target == 0:
                ret.append(cands.copy())
                return
            if target < 0 or i >= len(nums):
                return
            
            
            #use 
            cands.append(nums[i])
            dfs(i, target-nums[i])

            #dont use 
            cands.pop()
            dfs(i+1, target)

            return
        
        dfs(0, target)
        return ret