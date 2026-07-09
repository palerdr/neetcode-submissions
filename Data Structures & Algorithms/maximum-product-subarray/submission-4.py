class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        g = nums[0]
        pmp = nums[0]
        pl = nums[0]
        for num in nums[1:]:
            prmp = pmp
            prl = pl
            pmp = max(prmp*num,num,prl*num)
            pl = min(prmp*num,num, prl*num)
            if pmp > g:
                g = pmp

        return g