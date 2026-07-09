class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)
        adj = defaultdict(set)
        degrees = {}
        for word in words:
            for char in word:
                degrees[char] = 0
                
        for i in range(n-1):
            word1 = words[i]
            word2 = words[i+1]
            for j in range(min(len(word1),len(word2))):
                if word1[j] != word2[j]:
                    if word2[j] not in adj[word1[j]]:
                        degrees[word2[j]] += 1
                        adj[word1[j]].add(word2[j])
                    break
            else:
                if len(word1) > len(word2):
                    return ""
                
        q = collections.deque([c for c in degrees if degrees[c] == 0])
        ret = []

        while q:
            cur = q.popleft()
            ret.append(cur)

            for n in adj[cur]:
                degrees[n] -= 1
                if degrees[n] == 0:
                    q.append(n)

        if len(ret) != len(degrees):
            return ""

        return "".join(ret)





