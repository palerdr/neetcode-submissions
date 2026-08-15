class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)

        tmp = []
        result = []
        def dfs(i):
            if i >= n:
                result.append(tmp.copy())
            else:
                tmp.append(nums[i])
                dfs(i+1)

                tmp.pop()
                dfs(i+1)
        
        dfs(0)
        return result

