class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            if len(nums) == 1:
                return nums[0]
            return 0

        rob1, rob2 = 0,0

        for i in range(len(nums)-1):
            temp = max(rob2, rob1 + nums[i])
            rob1 = rob2
            rob2 = temp

        t1 = rob2

        rob1, rob2 = 0,0
        for i in range(1, len(nums)):
            temp = max(rob2, rob1 + nums[i])
            rob1 = rob2
            rob2 = temp

        t2 = rob2

        return max(t1,t2)

            