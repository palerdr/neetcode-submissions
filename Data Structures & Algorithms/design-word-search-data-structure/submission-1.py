class WordDictionary:

    def __init__(self):
        self.backing = set()


    def addWord(self, word: str) -> None:
        if not word:
            return
        ret = []
        temp = []

        def dfs(i,d): 
            if d < 0:
                return
            if i >= len(word):
                ret.append("".join(temp))
                return
            
            temp.append(".") #append . in place of the letter
            dfs(i+1,d-1)
            temp.pop()

            temp.append(word[i]) #use the letter as normal
            dfs(i+1,d)
            temp.pop()
        
        dfs(0, len(word)) #at most 2 dots
        
        for word in ret:
            self.backing.add(word)



    def search(self, word: str) -> bool:
        if not word:
            return False
        if word in self.backing:
            return True
        else:
            return False