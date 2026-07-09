class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        if len(s)%2 != 0:
            return False
        
        map = {"]":"[","}":"{",")":"("}
        if s[0] not in map.values():
            return False
        
        stack = []
        for c in s:
            if c in map:
                if stack and stack[-1] == map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
            
        return stack == []
