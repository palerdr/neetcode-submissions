class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            k,j = i,i
            while k >= 0 and j <= len(s)-1:
                if s[k]==s[j]:
                    res += 1
                    k-=1
                    j+=1    
                else:
                    break            
            k,j = i,i+1
            while k >=0 and j <= len(s)-1:
                if s[k]==s[j]:
                    res += 1
                    k-=1
                    j+=1    
                else:
                    break 

        return res


