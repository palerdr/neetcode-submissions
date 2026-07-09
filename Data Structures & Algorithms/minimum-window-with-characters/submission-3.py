class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #shortest substring of s with every character in t
        if len(t) > len(s):
            return ""

        counts = [0] * (ord('z') - ord('A') + 1)

        for character in t:
            counts[ord(character) - ord('A')] += 1
        
        min_window = float('inf')
        l_b, r_b = 0,0
        l = 0
        for r in range(len(s)):
            counts[ord(s[r]) - ord('A')] -= 1

            while all(count <= 0 for count in counts):
                
                if r-l+1 < min_window:
                    min_window = r-l+1
                    l_b = l
                    r_b = r

                counts[ord(s[l]) - ord('A')] += 1
                l+=1

        return s[l_b:r_b+1] if min_window != float('inf') else ""

