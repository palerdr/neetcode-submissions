class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solutions = []
        nums.sort()

        for i,num in enumerate(nums):
            if i > 0 and num == nums[i-1]: #duplicate for first term
                continue
            l,r =  i + 1, len(nums)-1
            target = -num
            while l<r:
                eq = nums[l] + nums[r]
                if eq == target:
                    solutions.append([nums[l],nums[r],nums[i]])
                    r -= 1
                    l += 1 
                    while l<r and nums[l] == nums[l-1]: #duplicate for second
                        l+=1
                    while l<r and nums[r] == nums[r+1]: #duplicate for third 
                        r-=1
                elif eq > target:
                    r -=1
                else:
                    l +=1

        return solutions
