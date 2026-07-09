class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        buckets = defaultdict(list)
        words = set(wordList)
        words.add(beginWord)
        n = len(beginWord)

        for word in words:
            for i in range(n):
                buckets[word[:i]+"#"+word[i+1:]].append(word)

        def get(word):
            for i in range(n):
                b = word[:i]+"#"+word[i+1:]
                for neighbor in buckets[b]:
                    if neighbor != word:
                        yield neighbor
        
        q = collections.deque()
        visited = set()
        q.append(beginWord)
        visited.add(beginWord)
        steps = 0

        while q:
            steps += 1
            for _ in range(len(q)):
                curr = q.popleft()
                if curr == endWord:
                    return steps
                for nei in get(curr):
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)

        return 0
        
        
            

