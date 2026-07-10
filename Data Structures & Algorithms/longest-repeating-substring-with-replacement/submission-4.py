from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1
        n = len(s)
        hf = 0 
        cf = {}
        l = 0
        for r in range(n):
            cf[s[r]] = cf.get(s[r], 0) + 1
            hf = max(hf, cf[s[r]])
            reps = (r - l + 1) - hf
            if (r - l + 1) - hf > k:
                cf[s[l]] -= 1
                l += 1
        
        return n - l

            




