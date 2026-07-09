class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        cands = []

        def dfs(i):
            ret.append(cands.copy())

            for j in range(i, len(nums)):
                if j > i and nums[j]==nums[j-1]:
                    continue
                cands.append(nums[j])
                dfs(j+1)
                cands.pop()

        dfs(0)
        return ret
