class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]

        for i in range(1, len(nums)):
            output.append(output[-1]*nums[i-1])
        
        post=1
        for j in range(len(nums)-2, -1 , -1):
            post *= nums[j+1]
            output[j] *= post

        return output