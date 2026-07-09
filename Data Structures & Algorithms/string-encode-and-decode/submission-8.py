class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        delimit = "!"
        for s in strs:
            marker = str(len(s))
            result.append(marker + delimit)
            result.append(s)
        return ''.join(result)

    def decode(self, s: str) -> List[str]:
        n = len(s)
        delimit = "!"
        res = []
        i = 0
        while i<n:
            j = i
            while s[j] != delimit:
                j += 1
            length = int(s[i:j])
            i=j+1
            res.append(s[i: i+length])
            i+=length
        return res



