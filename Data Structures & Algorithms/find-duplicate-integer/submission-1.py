class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: first find if there's an intersection in cycles
        tortoise = nums[0]
        hare = nums[0]
        
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        # Phase 2: know they will intersect, now loop finds where
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        return hare