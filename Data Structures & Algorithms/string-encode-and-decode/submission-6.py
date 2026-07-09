class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i, s in enumerate(strs):
            encoded +=  str(len(s)) + "$" + s
        return encoded 

    def decode(self, s: str) -> List[str]:
        decoded = []
        taker = ""
        i = 0
        while i <= len(s)-1:
            if s[i] == "$":
                decoded.append(s[i+1: i+1 + int(taker)]) #append from after signal length of taker
                i += int(taker) + 1 #jump to next word
                taker = "" #reset taker
            else: #number has multiple digits
                taker += s[i]
                i += 1
        return decoded