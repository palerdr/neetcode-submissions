class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        L = 1
        U = n+1
        def swap(i,j):
            nums[i],nums[j] = nums[j],nums[i]

        for i in range(n):
            while (1 <= nums[i] <= n) and nums[i] != i+1:
                if not(0<=nums[i]-1<=n-1) or nums[nums[i]-1] == nums[i]:
                    break
                swap(nums[i]-1, i)
            
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return U