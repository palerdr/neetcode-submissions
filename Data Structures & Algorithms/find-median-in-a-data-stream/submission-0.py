class MedianFinder:

    def __init__(self):
        self.store_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.store_heap, num)
        

    def findMedian(self) -> float:
        length = len(self.store_heap)

        if length % 2 == 0:
            parity = "even"
        else: 
            parity = "odd"

        work = self.store_heap.copy()
        if parity == "even":
            boundary = length//2 -1
        else:
            boundary = length//2

        for i in range(boundary):
            heapq.heappop(work)
        
        if parity == "even":
            a = heapq.heappop(work)
            b = heapq.heappop(work)
            return (a+b)/2
        else:
            return heapq.heappop(work)