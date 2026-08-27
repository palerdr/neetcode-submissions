class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq

        max_heap = []
        for x,y in points:
            sq_dist = - (x**2 + y**2)

            if len(max_heap) < k:
                heapq.heappush(max_heap, (sq_dist, [x,y]))
            else:
                heapq.heappushpop(max_heap, (sq_dist, [x,y]))

        
        return [point for dist,point in max_heap]



        