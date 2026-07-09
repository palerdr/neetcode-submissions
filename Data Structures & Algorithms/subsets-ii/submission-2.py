class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        p = []
        def dfs(i):
            ret.append(p.copy())
            for j in range(i,len(nums)):
                if j>i and nums[j] == nums[j-1]:
                    continue
                
                p.append(nums[j])
                dfs(j+1)
                p.pop()
                

        

        dfs(0)
        return ret
            
            