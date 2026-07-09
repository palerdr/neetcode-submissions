class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freqs = [0] * 2001
        #idx is the number
        freq_idx = [[] for _ in range(len(nums)+1)]
        #idx is the frequency need empty list at 0
        result = []
        #results list
        for num in nums:
            idx = num + 1000
            num_freqs[idx] += 1
        
        for i,freq in enumerate(num_freqs):
            if freq == 0:
                continue
            freq_idx[freq].append(i - 1000)

        while freq_idx and k > 0:
            popped = freq_idx.pop()
            result.extend(popped)
            k -= len(popped)

        return result
        




