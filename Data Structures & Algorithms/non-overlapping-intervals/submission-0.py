class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        n = len(intervals)
        intervals = sorted(intervals, key=lambda x:x[1])
        used = 0
        last_f = None
        for s,f in intervals:
            if not last_f:
                last_f = f
                used += 1
            elif s >= last_f:
                last_f = f
                used += 1
        return n - used