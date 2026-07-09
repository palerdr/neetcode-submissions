class WordDictionary:

    def __init__(self):
        self.trie = {}
        self.end = '#'

    def addWord(self, word: str) -> None:
        node = self.trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node[self.end] = True

    def search(self, word: str) -> bool:

        def dfs(i,node):
            if i >= len(word):
                return self.end in node

            char = word[i]
            if char == ".":
                for child,branch in node.items():
                    if child == self.end:
                        continue
                    if dfs(i+1, branch):
                        return True
            
            elif char in node:
                if dfs(i+1, node[char]):
                    return True
            
            return False
        
        return dfs(0,self.trie)
            
        
