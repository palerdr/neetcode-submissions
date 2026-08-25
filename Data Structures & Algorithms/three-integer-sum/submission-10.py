class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

            
        
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = -nums[i]

            l,r = i+1,n-1
            while l < r:
                s = nums[l] + nums[r]
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    result.append([nums[l], nums[r], nums[i]])

                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    
        
        return result




            