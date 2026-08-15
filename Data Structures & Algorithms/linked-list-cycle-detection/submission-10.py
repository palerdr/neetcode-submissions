# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head.next.next

        while fast != None:
            if slow == fast:
                return True
            else:
                slow = slow.next
                if not fast.next:
                    return False
                else:
                    fast = fast.next.next
        return False
