class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ret = []

        sub = []
        def dfs(i):
            if i >= len(nums):
                ret.append(sub.copy())
                return
            #include i 
            sub.append(nums[i])
            dfs(i+1)

            #don't include i
            sub.pop()
            dfs(i+1)
        
        dfs(0)

        return ret

            