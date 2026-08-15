# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        

        curr = None
        nxt = head

        while nxt is not None:
            tmp = nxt.next
            nxt.next = curr
            curr = nxt
            nxt = tmp
        
        return curr
