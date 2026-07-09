class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: #handles empty input case
            return 0 
        numset = set(nums) #more efficient membership checks with set
        longest = 1 #set length variable
        for num in numset:
            if num - 1 not in numset: #won't start counting if smaller starting
                length = 1 #resets count
                current = num #stores current value
                while current + 1 in numset:
                    length += 1 #updates both
                    current += 1 #updates both
                longest = max(longest, length) #updates longest
        return longest



