class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix = [1]
        #prefix product of all the numbers up to and NOT including index i

        acc = prefix[-1]
        for i in range(n-1):
            num = nums[i]
            acc = num * acc
            prefix.append(acc)
        
        #[1,2,4,6]
        #[1,1,2,8]

        acc = 1
        for i in range(n-1, -1, -1):
            num = nums[i]
            prefix[i] = acc * prefix[i]
            acc = num * acc
        
        return prefix


        


     