class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupes = set()
        for i,num in enumerate(nums):
            if num in dupes:
                return True
            else:
                dupes.add(num)
        return False