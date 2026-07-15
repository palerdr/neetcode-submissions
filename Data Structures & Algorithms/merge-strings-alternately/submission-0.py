class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = len(word1)
        n = len(word2)
        i,j,k = 0,0,0
        new = ['!'] * (n + m)
        flag = 0
        while k < n + m:
            if i > m - 1:
                new[k] = word2[j]
                j += 1
            elif j > n - 1:
                new[k] = word1[i]
                i += 1
            elif flag == 0:
                new[k] = word1[i]
                i += 1
                flag = 1
            else:
                new[k] = word2[j]
                j += 1
                flag = 0
            k += 1
        return ''.join(new)