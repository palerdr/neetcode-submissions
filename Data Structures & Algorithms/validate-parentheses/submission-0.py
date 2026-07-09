class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        elements = {')':'(', ']':'[', '}':'{'} # character bank
        for c in s:
            if c in elements:
                if stack and stack[-1] == elements[c]: #checks if in bank
                    stack.pop() #takes out if is
                else:
                    return False #if not not valid
            else:
                stack.append(c) #appends opening first way thru so check can match with closing in bank and pop
        return True if not stack else False      
