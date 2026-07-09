class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        ret = []
        forwards = self.permute(nums[1:])
        for perm in forwards:
            for i in range(len(nums)):
                c = perm.copy()
                c.insert(i, nums[0])
                ret.append(c)
        
        return ret
