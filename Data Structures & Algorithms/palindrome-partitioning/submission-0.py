class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def is_palindrome(string):
            l,r = 0, len(string)-1
            while l<=r:
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        pals = []
        tmp = []
        
        def dfs(i):
            if i >= len(s):
                pals.append(tmp.copy())
            
            for j in range(i+1, len(s)+1):
                pal = s[i:j]
                if is_palindrome(pal):
                    tmp.append(pal)
                    dfs(j)
                    tmp.pop()
        #we are partitioning the dfs at cuts
        
        dfs(0)

        return pals

        