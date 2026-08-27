class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq

        max_heap = []
        for x,y in points:
            sq_dist = x**2 + y**2
            #default min heap so must negate for a max heap
            if max_heap and len(max_heap) == k:
                if -sq_dist >= max_heap[0][0]:
                    heapq.heapreplace(max_heap, (-sq_dist, [x,y]))
            
            else:
                heapq.heappush(max_heap, (-sq_dist, [x,y]))


        
        return list(map(lambda x: x[1], max_heap))



        