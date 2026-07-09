class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        tot = 0
        for i, n in enumerate(nums):
            tot ^= n
        return tot

