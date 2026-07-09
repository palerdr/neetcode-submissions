class Solution:
    def countSubstrings(self, s: str) -> int:

        def countPal(k,j):
            res = 0
            while k >= 0 and j <= len(s)-1and s[k]==s[j]:
                res += 1
                k-=1
                j+=1
            return res
        
        r = 0
        for i in range(len(s)):
            k,j = i,i
            #first count odds
            r += countPal(k,j)
            #now count evens
            k,j = i,i+1
            r += countPal(k,j)

        return r


