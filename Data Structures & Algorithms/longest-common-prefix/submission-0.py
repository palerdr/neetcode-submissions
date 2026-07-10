class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        lcp = []
        #initialize the return array as empty
        sl = len(strs[0])
        for s in strs:
            sl = min(sl, len(s))
        #find the shortest string length in the list

        #loop over range of shortest string
        #store the character from the first string at this index
        #check if all the strs have that should be at the index
        #at the first time the strings all differ we break both loops
        for j in range(sl):
            tmp = strs[0][j]
            in_all = True
            for i in range(len(strs)):
                if strs[i][j] != tmp:
                    in_all = False
                    break
            if in_all:
                lcp.append(tmp)
            else:
                break
        
        return "".join(lcp)
                
                
       
                

        