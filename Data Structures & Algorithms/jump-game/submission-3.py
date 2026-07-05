class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        
        lgp = n-1
        for i in range(n-1, -1, -1):
            if i + nums[i] >= lgp:
                lgp = i
            
        return lgp == 0


