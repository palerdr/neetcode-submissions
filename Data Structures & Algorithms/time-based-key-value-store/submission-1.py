class TimeMap:

    def __init__(self):
        self.Timemapping = defaultdict(list)
        

    def set(self, key, value, timestamp) -> None:
        self.Timemapping[key].append((value,timestamp))
        

    def get(self, key, timestamp) -> str:
        if key not in self.Timemapping:
            return ""

        values = self.Timemapping[key]
        l,r = 0,len(values)-1
        res = ""
        while l<=r:
            m = (l+r)//2
            time = values[m][1]
            value = values[m][0]
            if time <= timestamp:
                res = value
                l = m+1
            else:
                r = m-1
        return res
                