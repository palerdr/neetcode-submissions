class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        store = [0] * 26

        def index_store(c): return ord(c) - ord('a')

        for c in magazine:
            store[index_store(c)] += 1

        for c in ransomNote:
            if store[index_store(c)] <= 0:
                return False
            else:
                store[index_store(c)] -= 1
        return True


        