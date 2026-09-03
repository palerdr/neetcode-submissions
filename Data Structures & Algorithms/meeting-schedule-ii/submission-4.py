"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        import heapq
        intervals = sorted(intervals, key=lambda x: x.start)
        heap = []
        # I will keep a min heap of the soonest ending meeting
        # for each meeting room

        for interval in intervals:
            s_i, f_i = interval.start, interval.end
            if not heap:
                heapq.heappush(heap, f_i)
            else:
                f_j = heap[0]
                if f_j <= s_i:
                    heapq.heapreplace(heap, f_i)
                else:
                    heapq.heappush(heap, f_i)


        return len(heap)










        