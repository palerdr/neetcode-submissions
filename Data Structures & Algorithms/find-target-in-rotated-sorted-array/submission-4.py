class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        while l<=r:
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[l]: #left side sorted
                if nums[l] <= target <= nums[mid]: #is in sorted part
                    r = mid -1 
                else: #not in sorted part search right
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid+1
                else:
                    r = mid - 1
        return -1