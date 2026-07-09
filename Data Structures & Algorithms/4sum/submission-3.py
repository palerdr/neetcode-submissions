class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def twoSum(nums, start, target):
            n = len(nums)
            #nums.sort()
            result = []
            l,r = start,n-1
            while l<r:
                twosum = nums[l] + nums[r]
                if twosum > target:
                    r-=1
                elif twosum < target:
                    l+=1
                else:
                    result.append([nums[l], nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
                    while l<r and nums[r] == nums[r+1]:
                        r-=1
            return result
        
        def kSum(nums, target, start, k):
            n = len(nums)
            #nums.sort()
            result = []
            if k == 2:
                return twoSum(nums, start, target)
            
            for i in range(start, n):
                if i > start and nums[i] == nums[i-1]:
                    continue
                for subset in kSum(nums, target - nums[i], i + 1, k - 1):
                    result.append([nums[i]] + subset)
            return result

        nums.sort()
        return kSum(nums, target, 0, 4)
