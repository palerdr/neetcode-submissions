class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        buckets = defaultdict(list)
        words = set(wordList)
        words.add(beginWord)
        n = len(beginWord)
        #generate buckets for each word
        for word in words:
            for i in range(n):
                buckets[word[:i]+"#"+word[i+1:]].append(word)
        #generator for the neighbors in the buckets a word is part of 
        def get(word):
            for i in range(n):
                b = word[:i]+"#"+word[i+1:]
                for neighbor in buckets[b]:
                    if neighbor != word:
                        yield neighbor
        #instantiate queue, visited set, and steps counter
        q = collections.deque()
        visited = set()
        q.append(beginWord)
        visited.add(beginWord)
        steps = 0
        #BFS guarantees minimum, level order process nodes and call generator
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
        
        
            

