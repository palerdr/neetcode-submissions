class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = len(word1)
        n = len(word2)
        i,j,k = 0,0,0
        new = ['!'] * (n + m)
        while k < n + m:
            if i > m - 1:
                new[k] = word2[j]
                j += 1
                k += 1
            elif j > n - 1:
                new[k] = word1[i]
                i += 1
                k += 1
            else:
                if i < m:
                    new[k] = word1[i]
                    i += 1
                    k += 1
                if j < n:
                    new[k] = word2[j]
                    j += 1
                    k += 1

        return ''.join(new)