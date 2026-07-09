class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        l = 0
        limit = len(s1)
        
        s1f = [0]*26
        for c in s1:
            s1f[ord(c)-ord("a")] += 1
        
        s2sf = [0]*26
        for r,c in enumerate(s2):
            s2sf[ord(c)-ord("a")] += 1

            while r-l+1 > limit:
                s2sf[ord(s2[l])-ord("a")] -= 1
                l+=1
            if s1f == s2sf:
                return True
        return False

        