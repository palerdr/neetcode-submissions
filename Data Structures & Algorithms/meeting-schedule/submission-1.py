"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key= lambda x : x.end)

        last_finish = float('-inf')
        for interval in intervals:
            si, fi = interval.start, interval.end
            if si >= last_finish:
                last_finish = fi
            else:
                return False
        
        return True
