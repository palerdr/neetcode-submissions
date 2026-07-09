class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            dist = (0-x)**2 + (0-y)**2
            heapq.heappush(h, (dist,i))
        
        ret = []
        for j in range(k):
            index = heapq.heappop(h)[1]
            ret.append(points[index])
        
        return ret
