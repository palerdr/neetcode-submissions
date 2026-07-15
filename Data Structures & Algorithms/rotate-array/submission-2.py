class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        nums.reverse()
        k = k % n
        def r(l,r):
            while l<r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        r(0, k-1)
        r(k, n-1)
