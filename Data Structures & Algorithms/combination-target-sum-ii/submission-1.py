class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(candidates)
        ret = []
        cands = []

        def dfs(i, target):
            if target == 0:
                ret.append(cands.copy())
                return
            if target < 0 or i >= len(nums):
                return

            cands.append(nums[i]) 
            dfs(i+1, target - nums[i])

            cands.pop()
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1, target)

        dfs(0, target)

        return ret
            
                    
            

