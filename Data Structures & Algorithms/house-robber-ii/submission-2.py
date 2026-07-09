class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        def robber(j, k):
            rob1,rob2 = 0,0
            for i in range(j, k):
                num = nums[i]
                temp = max(num + rob1, rob2)
                rob1, rob2 = rob2, temp
            return rob2
        
        return max(robber(0,n-1), robber(1,n))