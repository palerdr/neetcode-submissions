class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        shortest = ""
        needed = Counter(t)
        missing = len(t) #should be the total of frequencies in t
        l = 0
        

        for r, char in enumerate(s):
            if needed[char] > 0:
                missing -= 1
            needed[char] -= 1
            
            while missing == 0: #we have all inside so we can shrink the window
                if len(shortest) == 0 or r-l+1 <= len(shortest):
                    shortest = s[l:r+1]
                if needed[s[l]] == 0 and s[l] in t: #don't need any but removing one
                    missing += 1
                needed[s[l]] += 1 
                l+=1

        return shortest
            
            
            