class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        r = []

        intervals = sorted(intervals, key= lambda x : x[0])
        for i,interval in enumerate(intervals):
            if not r or r[-1][1] < interval[0]:
                r.append(interval)
            
            a = r.pop()
            a_start, a_end = a[0], a[1]
            b_start, b_end = interval[0], interval[1]

            r.append([
                min(a_start, b_start),
                max(a_end, b_end),
            ])

        return r
        