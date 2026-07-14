# Linear Probing HashMap
class MyHashMap:
    def __init__(self):
        self.cap = 10
        self.buckets = [None] * self.cap
        self.size = 0
        self.lf = 0.75
        self.TOMBSTONE = object()
        
    def _hash(self, key):
        return key % self.cap
    
    def _rehash(self):
        tmp = self.buckets
        self.cap = self.cap * 2
        self.buckets = [None] * self.cap
        self.size = 0
        for item in tmp:
            if item is not None and item is not self.TOMBSTONE:
                (k, v) = item
                self._insert(k, v)
    
    def _insert(self, key, value):
        idx = self._hash(key)
        k = idx
        updating = False
        while self.buckets[k] is not None:
            if self.buckets[k] is not self.TOMBSTONE:
                if self.buckets[k][0] == key:
                    updating = True
                    break
            k = (k + 1) % self.cap
            
        self.buckets[k] = (key, value)
        self.size += 0 if updating else 1

    def put(self, key: int, value: int) -> None:
        if (self.size + 1) / self.cap > self.lf:
            self._rehash()
        self._insert(key, value)

    def get(self, key: int) -> int:
        idx = self._hash(key)
        k = idx
        while self.buckets[k] is not None:
            if self.buckets[k] is not self.TOMBSTONE:
                if self.buckets[k][0] == key:
                    return self.buckets[k][1]
            k = (k + 1) % self.cap
        return -1
        

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        k = idx
        while self.buckets[k] is not None:
            if self.buckets[k] is not self.TOMBSTONE:
                if self.buckets[k][0] == key:
                    self.buckets[k] = self.TOMBSTONE
                    return
            k = (k + 1) % self.cap
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)