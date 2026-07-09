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
        backing = {}

        prev = None
        curr = head
        
        while curr != None:
            backing[curr] = Node(curr.val)
            if prev is not None:
                backing[prev].next = backing[curr]
            prev = curr
            curr = curr.next
        
        curr = head
        while curr != None:
            if curr.random is not None:
                backing[curr].random = backing[curr.random]
            curr = curr.next
        
        return backing[head]