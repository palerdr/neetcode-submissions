class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        store = {}

        for i in range(len(nums)):
            num = nums[i]
            diff = target - num
            if diff in store:
                return [store[diff], i]
            else: 
                store[num] = i
