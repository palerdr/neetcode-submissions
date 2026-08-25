class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

            
        

        def kSum(nums: List[int], target: int, k: int, start_idx):
            """must be called on a sorted array"""
            result = []
            n = len(nums)

            if k == 2:
                
                l,r = start_idx,n-1
                while l < r:
                    if nums[l] + nums[r] < target:
                        l += 1
                    elif nums[l] + nums[r] > target:
                        r -=1
                    else:
                        result.append([nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1

                return result
                    

                
            for i in range(start_idx, n - k + 1):
                if i > start_idx and nums[i] == nums[i-1]:
                    continue
                
                result.extend(
                    [[nums[i]] + sol for sol in kSum(nums, target - nums[i], k - 1, i + 1)]
                )
            
            return result
        
        nums.sort()
        return kSum(nums, 0, 3, 0)




            