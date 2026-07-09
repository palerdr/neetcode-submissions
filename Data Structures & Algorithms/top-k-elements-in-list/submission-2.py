class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)
        buckets = [[] for _ in range(len(nums)+1)] #include 0
        
        for num,count in counts.items():
            buckets[count].append(num)
        ret = []
        for i in range(len(buckets)-1, -1, -1):
            for num in buckets[i]:
                ret.append(num)
                k -= 1
                if k == 0:
                    return ret 





        