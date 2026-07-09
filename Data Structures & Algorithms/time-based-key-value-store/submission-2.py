class TimeMap:

    def __init__(self):
        self.store = {}

        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append((timestamp,value))
        else:
            self.store[key] = [(timestamp,value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        pairs = self.store[key]
        l,r = 0, len(pairs)-1
        ret = ""
        
        while l <= r:
            m = (l+r)//2
            if pairs[m][0] <= timestamp:
                ret = pairs[m][1]
                l = m+1
                #search for a more recent one
            else:
                r = m-1
        return ret

        
