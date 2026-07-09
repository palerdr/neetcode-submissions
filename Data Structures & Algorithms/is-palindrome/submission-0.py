class Solution:
    def isPalindrome(self, s: str) -> bool:
        full = ''.join(c.lower() for c in s if c.isalnum()) #full normalized string
        return full == full[::-1] #check if right forward and back
