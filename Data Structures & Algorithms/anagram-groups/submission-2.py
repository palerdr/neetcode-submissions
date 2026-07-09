class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        counts = {}

        for string in strs:
            letter_counts = [0]*26
            for letter in string:
                letter_counts[ord(letter) - ord('a')] += 1
            ckey = tuple(letter_counts)
            if ckey in counts:
                counts[ckey].append(string)
            else:
                counts[ckey] = [string]
        
        return list(counts.values())

        
