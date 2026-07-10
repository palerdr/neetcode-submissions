class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        from functools import reduce
        return reduce(lambda acc, num: acc + [[num] + subset for subset in acc], nums, [[]])