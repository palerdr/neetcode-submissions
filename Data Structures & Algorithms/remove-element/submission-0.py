class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        k = 0
        while nums:
            try:
                nums.remove(val)
                k += 1
            except ValueError:
                break
                
        return n-k
