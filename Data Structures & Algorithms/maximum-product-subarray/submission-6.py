class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mp = nums[0]
        pmp = mp
        plp = mp

        for num in nums[1:]:
            tmp1 = pmp
            tmp2 = plp
            #max = max(lowest*i, max*i, starting new at i)
            #min = min(same as ^^)
            pmp = max(num*tmp1, num*tmp2, num)
            plp = min(num*tmp1, num*tmp2, num)
            mp  = max(pmp,mp)
        return mp