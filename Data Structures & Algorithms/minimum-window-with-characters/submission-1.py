class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        
        tf = [0]*52 #frequency map of characters in s
        for c in t:
            if c.islower():
                idx = ord(c) - ord('a')
            else:
                idx = 26 + (ord(c) - ord('A'))
            tf[idx] += 1

        l = 0
        ssubf = [0]*52
        contains = False
        shortest = ""
    
        for r, char in enumerate(s):
            if char.islower():
                idx = ord(char) - ord('a')
            else:
                idx = 26 + (ord(char) - ord('A'))
            ssubf[idx] += 1

            for i in range(52):
                if tf[i] == 0:
                    continue
                else:
                    if tf[i] <= ssubf[i]:
                        contains = True
                    else:
                        contains = False
                        break
                    
            while contains:
                if shortest == "" or len(shortest) >= r-l+1:
                    shortest = s[l:r+1]
                if s[l].islower():
                    idx = ord(s[l]) - ord('a')
                else:
                    idx = 26 + (ord(s[l]) - ord('A'))
                ssubf[idx] -= 1
                l += 1
                for i in range(52):
                    if tf[i] == 0:
                        continue
                    else:
                        if tf[i] <= ssubf[i]:
                            contains = True
                        else:
                            contains = False
                            break
        return shortest
            
            