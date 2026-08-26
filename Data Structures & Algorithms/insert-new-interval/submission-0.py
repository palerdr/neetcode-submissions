class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if not intervals:
            return [newInterval]

        n = len(intervals)
        r = []

        b_start, b_end = newInterval[0], newInterval[1]
        i = 0
        while i < n:
            a_start, a_end = intervals[i][0], intervals[i][1]

            if a_end < b_start:
                r.append(intervals[i])
                i += 1
            
            elif b_end < a_start:
                
                break
            
            else:
                b_start = min(a_start, b_start)
                b_end = max(a_end, b_end)
                i += 1

        r.append([b_start, b_end])
        while i < n:
            r.append(intervals[i])
            i += 1

        return r


            


            
