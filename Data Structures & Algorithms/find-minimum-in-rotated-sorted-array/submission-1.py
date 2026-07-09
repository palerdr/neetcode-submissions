class Solution:
    def findMin(self, nums: List[int]) -> int:
        smallest = nums[0] #if rotated 0 or n number length times itll just be first
        l,r = 0, len(nums)-1
        while l<=r:
            if nums[l] < nums[r]: #if subarray is sorted it will just be leftmost
                smallest = min(smallest, nums[l])
                break #leave loop
            mid = (l+r)//2
            smallest = min(smallest, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid -1
        return smallest 
                