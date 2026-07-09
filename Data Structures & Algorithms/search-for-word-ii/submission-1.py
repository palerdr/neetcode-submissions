class Solution:
    class Trie:
        def __init__(self):
            self.trie = {}
            self.end = "#"
        def insert(self,word):
            node = self.trie
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node[self.end] = word
        def search(self,word):
            node = self.trie
            for char in word:
                if char not in node:
                    return False
                node = node[char]
            return self.end in node
        def startsWith(self,prefix):
            node = self.trie
            for char in prefix:
                if char not in node:
                    return False
                node = node[char]
            return True

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        found = Solution.Trie()
        ret = []
        n = len(board)
        m = len(board[0])

        temp = []
        def dfs(i,j,root):
            if not (-1 < i < n and -1 < j < m):
                return
                
            c = board[i][j]

            if c not in root or c == "!": #mismatch or used already
                return
            temp.append(c)
            board[i][j] = '!'
            nxt = root[c]

            if '#' in nxt:
                ret.append(nxt['#'])
                del nxt['#']
                #must keep exploring
             
            dfs(i+1,j,nxt)
            dfs(i-1,j,nxt)
            dfs(i,j+1,nxt)
            dfs(i,j-1,nxt)
            temp.pop()
            board[i][j] = c

        for word in words:
            found.insert(word)

        for i in range(n):
            for j in range(m):
                dfs(i,j,found.trie)

        return ret





































        