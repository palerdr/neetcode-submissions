class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set() #empty set
        l = 0 
        longest = 0
        for r in range(len(s)):
            while s[r] in chars: #check set for membership
                chars.remove(s[l]) #removes until duplicate is gone then adds to longest
                l += 1
            chars.add(s[r]) #if not in adds to the set
            longest = max(longest, r - l + 1) #make sure not overwriting when smaller
        return longest

