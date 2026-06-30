class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if not nums:
            return []
        
        cutoff = n/3
        result = []

        c1, c2 = None, None
        v1, v2 = 0,0
        for num in nums:
            if num == c1:
                v1 += 1
            elif num == c2:
                v2 += 1
            elif v1 == 0:
                c1 = num
                v1 = 1
            elif v2 == 0:
                c2 = num
                v2 = 1
            else:
                v1 -= 1
                v2 -= 1
            
        result = []
        f1,f2 = 0,0
        for num in nums:
            if num == c1:
                f1 += 1
            elif num == c2:
                f2 += 1

        if f1 > cutoff:
            result.append(c1)
        
        if f2 > cutoff:
            result.append(c2)

        return result
            




