class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1]
        postfix = [1]
        for num in nums:
            prefix.append(num * prefix[-1])
        prefix.pop()
        
        for num in reversed(nums):
            postfix.append(num * postfix[-1])
        postfix.pop()
        postfix.reverse()

        for i in range(n):
            nums[i] = prefix[i] * postfix[i]

        return nums
             
