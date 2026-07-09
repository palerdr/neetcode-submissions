class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list) # set up accumulator dict, if key not exist empty list
        for word in strs: # outer iteration for each word
            key = ''.join(sorted(word)) #generates key by joining alphabetical list of characters
            output[key].append(word) #adds word to list at key, adds to empty if not anagram
        return list(output.values()) # returns just the sublists organzied by key
           