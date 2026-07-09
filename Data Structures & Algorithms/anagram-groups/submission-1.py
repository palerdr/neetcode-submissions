class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = defaultdict(list)
        for i, word in enumerate(strs):
            count = [0]*26
            for c in word:
                count[ord(c)-ord("a")] += 1
            grouped[tuple(count)].append(word)
        return list(grouped.values())