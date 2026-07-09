class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int) #dictionary with default integer value
        for num in nums: #loops thru list
                freq[num] += 1 #handles frequency
        return [key for key, count in sorted(freq.items(), key=lambda x: x[1], reverse=True)[:k]]
        #sorts into tuples sorted by frequency descending and then returns list of the top k keys