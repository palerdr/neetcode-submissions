class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        dists = defaultdict(int)

        res = 0
        for num in nums:
            if not dists[num]:
                dists[num] = dists[num-1] + dists[num+1] + 1
                #this is connecting 2 must update them too
                dists[num + dists[num+1]] = dists[num]
                dists[num - dists[num-1]] = dists[num]
                res = max(res, dists[num])
        
        return res
        