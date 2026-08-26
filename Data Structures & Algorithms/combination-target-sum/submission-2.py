class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        n = len(nums)

        res = []
        tmp = []
        nums.sort()
        
        def dfs(i, running_sum):
            if i >= n:
                return
            
            num = nums[i]
            if num > target:
                return
            
            new_sum = running_sum + num

            if new_sum == target:
                tmp.append(num)
                res.append(tmp[:])
                tmp.pop()

            elif new_sum < target:
                tmp.append(num)
                dfs(i, new_sum)
                tmp.pop()
                dfs(i+1, running_sum)
        
        dfs(0, 0)

        return res
            
            
            

        