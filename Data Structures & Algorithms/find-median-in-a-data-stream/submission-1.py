class MedianFinder:

    def __init__(self):
        self.lo_heap = []
        #keeps track of the max of the lower half
        self.hi_heap = []
        #keeps track of the min of the upper half

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lo_heap, -num)

        #must ensure each half is increasing ordering
        if self.lo_heap and self.hi_heap and -self.lo_heap[0] > self.hi_heap[0]:
            heapq.heappush(self.hi_heap, -heapq.heappop(self.lo_heap))

        #must ensure that the low heap is always 1 or 0 more than the high heap
        if len(self.lo_heap) > len(self.hi_heap) + 1:
            heapq.heappush(self.hi_heap, -heapq.heappop(self.lo_heap))
        elif len(self.hi_heap) > len(self.lo_heap):
            heapq.heappush(self.lo_heap, -heapq.heappop(self.hi_heap))


    def findMedian(self) -> float:
        if len(self.lo_heap) > len(self.hi_heap):
            return -self.lo_heap[0]
        else:
            return (-self.lo_heap[0] + self.hi_heap[0]) /2
        