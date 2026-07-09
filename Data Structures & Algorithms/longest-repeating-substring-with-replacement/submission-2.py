class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        longest = 0 
        mostf = 0
        freq = defaultdict(int)
        
        for r,char in enumerate(s):
            freq[char] +=1
            mostf = max(freq[char], mostf)
            while r-l+1 - mostf > k:
                freq[s[l]] -=1
                l += 1
            longest = max(r-l+1, longest)
        return longest
        