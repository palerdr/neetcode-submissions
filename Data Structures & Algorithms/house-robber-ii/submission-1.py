class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1F, rob2F = 0,0
        rob1, rob2 =0,0

        for i in range(len(nums)):
            num = nums[i]
            if i == len(nums)-1:
                temp = max(num + rob1, rob2)
                rob1 = rob2
                rob2 = temp
                continue
            if i == 0:
                tempF = max(num + rob1F, rob2F)
                rob1F = rob2F 
                rob2F = tempF
                continue

            tempF = max(num + rob1F, rob2F)
            rob1F = rob2F 
            rob2F = tempF

            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        return max(rob2, rob2F)