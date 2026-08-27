class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq

        def dist(x1, y1, x2, y2):
            return ((x1-x2)**2 + (y1-y2)**2)

        return heapq.nsmallest(
            k,
            points,
            key = lambda point: dist(0,0,point[0],point[1])
        )


        