# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        list_length = 0

        tl = ListNode(0)
        tl.next = head

        while tl.next is not None:
            tl = tl.next 
            list_length += 1

        updates_to_mid = (list_length // 2) + 1
        
        hd = ListNode(0)
        hd.next = head

        while updates_to_mid > 0:
            hd = hd.next
            updates_to_mid -= 1
        
        return hd