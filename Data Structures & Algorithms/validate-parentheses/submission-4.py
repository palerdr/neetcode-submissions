class Solution:
    def isValid(self, s: str) -> bool:
        store = {
            ")" : "(",
            "}" : "{",
            "]" : "[",
        } 

        stack = []
        
        for brace in s:
            if not stack:
                if brace in store:
                    return False
                else:
                    stack.append(brace)
            else:
                if brace in store:
                    if stack[-1] == store[brace]:
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(brace)

        
        return not stack
