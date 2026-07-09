class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Topk = [[] for i in range(len(nums)+1)]

        for num,count in Counter(nums).items():
            Topk[count].append(num)
        
        res = []
        for i in range(len(Topk)-1, 0 ,-1): #right to left 
            for n in Topk[i]:
                res.append(n)
                if len(res) == k:
                    return res