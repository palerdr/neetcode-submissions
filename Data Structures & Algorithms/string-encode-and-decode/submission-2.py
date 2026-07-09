class Solution:

    def encode(self, strs: List[str]) -> str:
        st = '' #sets output string to add to
        for s in strs: #iterate over each string
            st += str(len(s)) + ';' + s #encode length of string and flag
        return st 
    def decode(self, s: str) -> List[str]:
        lst = [] #sets output list
        i = 0  
        while i < len(s): #iterate through string
            j = i
            while s[j] != ';': #reads full length of number up to ;
                j+=1 # update loop variable, finds first ; to execute length
            length = int(s[i:j]) #store length
            word = s[j+1:j+length+1] #store word adding length
            lst.append(word) #add word to list
            i = j + length + 1 #update loop variables
        return lst