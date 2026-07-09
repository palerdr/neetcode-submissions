class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        longest = 0
        for i,num in enumerate(nums):
            if num-1 in numbers:
                continue
            #if we clear this we are at the start of a sequence
            temp = 1
            i = num + 1 # is the next number in our set
            while i in numbers:
                i += 1 
                temp += 1
            longest = max(temp,longest)
        return longest
