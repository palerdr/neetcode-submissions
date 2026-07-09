class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []

        temp = []

        def dfs(i, t):
            if i >= len(nums) or t <= 0: 
                if t == 0:
                    ret.append(temp.copy())
                return

            temp.append(nums[i])
            dfs(i, t-nums[i])

            temp.pop()
            dfs(i+1, t)

            return
        
        dfs(0,target)
        return ret