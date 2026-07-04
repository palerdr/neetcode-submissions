class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        store = {}
        longest_cons = 0
        for num in nums:
            if num in store:
                continue
            lt = store.get(num-1, 0)
            rt = store.get(num+1, 0)
            tot = lt + rt + 1
            longest_cons = max(longest_cons, tot)
            store[num] = tot
            store[num - lt] = tot
            store[num + rt] = tot
        return longest_cons
