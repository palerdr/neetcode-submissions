class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = []

        for stone in stones:
            heapq.heappush(q, -stone)
        
        while len(q) > 1:
            s1 = -heapq.heappop(q)
            s2 = -heapq.heappop(q)

            if s1 == s2:
                continue
            
            larger = max(s1,s2)
            smaller = min(s1,s2)
            larger -= smaller
            heapq.heappush(q, - larger)

        if not q:
            return 0
        return -q[0]