class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        schars = {} # dict for all characters in s 
        tchars = {} # dict for all characters in t
        for char in s: #iterate through s
            if char not in schars:
                schars[char] = 1
            else:
                schars[char] += 1
        for char in t: #iterate through t
            if char not in tchars:
                tchars[char] = 1
            else:
                tchars[char] += 1
        return schars == tchars # return condition