class LinkedList:
        def __init__(self, key, nxt=None):
            self.key = key
            self.nxt = nxt 

class MyHashSet:  

    def __init__(self):
        self.buckets = [None] * 1000
    
    def _hash(self, key):
        return key % 1000

    def add(self, key: int) -> None:
        idx = self._hash(key)
        node = self.buckets[idx]
        if node is None:
            self.buckets[idx] = LinkedList(key)
        else:
            while True:
                if node.key == key:
                    return
                elif node.nxt is None:
                    break
                node = node.nxt
            node.nxt = LinkedList(key)

    def remove(self, key: int) -> None:
        idx = self._hash(key)
        node = self.buckets[idx]
        if node is None:
            return
        elif node.key == key:
            self.buckets[idx] = node.nxt
            return 
        else:
            while node.nxt is not None:
                if node.nxt.key == key:
                    node.nxt = node.nxt.nxt
                    return
                node = node.nxt

    def contains(self, key: int) -> bool:
        idx = self._hash(key)
        node = self.buckets[idx]
        while node is not None:
            if node.key == key:
                return True
            node = node.nxt
        return False

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)