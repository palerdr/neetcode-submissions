class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = {}
        for s in strs:
            key = [0] * 26
            for c in s:
                key[ord(c) - ord('a')] += 1
            new_key = tuple(key) 
            if new_key in store:
                store[new_key].append(s)
            else:
                store[new_key] = [s]
        return list(store.values())


