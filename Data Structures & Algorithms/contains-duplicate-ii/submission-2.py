class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        def almost_dupe(i,j):
            return nums[i] == nums[j] and abs(i - j) <= k
        store = {}

        
        for i, num in enumerate(nums):
            if num in store:
                j = store[num]
                if almost_dupe(i,j):
                    return True
            store[num] = i
        
        return False
        
