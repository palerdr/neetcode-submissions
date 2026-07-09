class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(candidates)
        ret = []
        
        def dfs(i, p, s):
            if s == target:
                ret.append(p.copy())
                return

            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                if s + nums[j] > target:
                    break
                    
                p.append(nums[j])
                dfs(j+1, p, s+nums[j])
                p.pop()

            return
        dfs(0,[],0)
        
        return ret

                