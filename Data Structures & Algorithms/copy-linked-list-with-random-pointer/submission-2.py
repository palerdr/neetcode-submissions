"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        backing = collections.defaultdict(lambda: Node(0))
        backing[None] = None

        
        curr = head
        
        while curr:
            backing[curr].val = curr.val
            backing[curr].next = backing[curr.next]
            backing[curr].random = backing[curr.random]
            curr = curr.next
        
        return backing[head]