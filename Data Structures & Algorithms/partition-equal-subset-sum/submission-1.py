class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False       

        dp = set()
        dp.add(0)
        target = sum(nums)//2
        for num in reversed(nums):
            nDP = set()
            for sol in dp:
                nDP.add(sol+num)
                nDP.add(sol)
            dp = nDP  
            #invariant is does any possible subset add up to sum over two?
        return True if target in dp else False

