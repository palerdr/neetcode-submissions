class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        schars = []
        tchars = []
        for i,char in enumerate(s):
            schars.append(char)
        for j, char in enumerate(t):
            tchars.append(char)
        return sorted([c.lower() for c in schars]) == sorted([c.lower() for c in tchars])