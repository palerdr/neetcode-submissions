class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, longest, mostf = 0,0,0
        #need a left pointer, return variable, and variable to store most frequent char in a substring
        freq = defaultdict(int)
        #initialize counter dictionary
        for r,char in enumerate(s):
            freq[char] +=1 #increment current char frequency
            mostf = max(freq[char], mostf) #update most frequent character in this substring
            while r-l+1 - mostf > k: #if we cannot reach this length with swaps must shrink
                freq[s[l]] -=1 #update freq
                l += 1 #update pointer
            longest = max(r-l+1, longest) #update gloabl return 
        return longest
        