class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:return False
        tgt = sum(nums)//2
        dp = 1<<0
        #sets the 0th bit to 1/True because we can always make a subset of 0
        #if we can make an arbitrary amount of subsets sum to number
        #we can always just join multiple subsets to make up the other half
        for num in nums:
            dp |= (dp<<num)
        return (dp & (1 << tgt)) != 0