class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        def almost_dupe(i,j):
            return nums[i] == nums[j] and abs(i - j) <= k
        
        j = 0
        for i in range(1, n):
            while j < i:
                if almost_dupe(i,j):
                    return True
                j += 1
            j = 0
        return False
        
