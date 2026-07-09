class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        dupes = set()
        longest_non = 0

        l = 0
        for i in range(len(s)):
            char = s[i]
            while char in dupes:
                dupes.remove(s[l])
                l += 1
            dupes.add(char)
            longest_non = max(longest_non, i-l+1)

        return longest_non
