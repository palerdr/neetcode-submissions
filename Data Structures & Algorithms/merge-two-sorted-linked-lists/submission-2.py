# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            if not list1:
                return list2
            else:
                return list1
        hd = ListNode(0)
        dummy = hd

        while list1 and list2:
            if list1.val < list2.val:
                dummy.next = list1
                dummy = dummy.next
                list1 = list1.next
            else:
                dummy.next = list2
                dummy = dummy.next
                list2 = list2.next

        dummy.next = list1 if list1 else list2

        return hd.next