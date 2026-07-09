class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(candidates)
        ret = []
        cands = []

        def dfs(i, target):
            if target == 0:
                if cands not in ret:
                    ret.append(cands.copy())
                return
            if target < 0 or i >= len(nums):
                return

            cands.append(nums[i]) 
            dfs(i+1, target - nums[i])

            cands.pop()
            dfs(i+1, target)

        dfs(0, target)

        return ret
            
                    
            

