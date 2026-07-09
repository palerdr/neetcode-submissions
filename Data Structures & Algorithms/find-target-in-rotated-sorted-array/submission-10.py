class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l,r = 0,len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m] > nums[l]:
                l = m
            elif nums[m] < nums[r]:
                r=m
            else:
                break
        cut = l

        l,r= 0,cut
        while l<=r:
            m = (l+r)//2
            if nums[m] > target:
                r=m-1
            elif nums[m] < target:
                l=m+1
            else:
                return m
        
        l,r= cut+1,len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m] > target:
                r=m-1
            elif nums[m] < target:
                l=m+1
            else:
                return m

        return -1

