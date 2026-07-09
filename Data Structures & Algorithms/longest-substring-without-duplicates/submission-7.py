class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l,r = 0,0
        used = set()

        while r < len(s):
            used.add(s[l])
            if r == l:
                r+=1
            elif s[r] in used:
                used.remove(s[l])
                l+=1
            else: 
                used.add(s[r])
                r+=1
            longest = max(longest,r-l)

        return longest

        
