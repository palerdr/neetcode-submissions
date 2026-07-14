class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)  
        t = n / 2

        candidate = None
        count = 0
        for num in nums:
            if count == 0 or candidate is None:
                candidate = num
            elif candidate is not None and num != candidate:
                count -= 1
                continue
            count += 1
        
        return candidate 

        
