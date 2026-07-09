class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [] #set up output list
        for i in range(len(nums)):
            x = 1 #start with product being 1 
            for j in range(len(nums)):
                if i != j: #handles case where we want to multiply
                    x *= nums[j]
            output.append(x)    
        return output