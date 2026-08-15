class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0,len(s)-1
        while l <= r:
            lchar = s[l]
            rchar = s[r]
            if not lchar.isalnum():
                l += 1
                continue
            else:
                if not rchar.isalnum():
                    r -= 1
                    continue
                else:
                    if lchar.lower() != rchar.lower():
                        return False
                    l += 1
                    r -= 1
        return True