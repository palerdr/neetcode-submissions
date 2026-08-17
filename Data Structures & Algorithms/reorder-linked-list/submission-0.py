# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        #O(N)
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #slow is always the last node of the first half
        mid = slow.next
        slow.next = None

        def reversed_ll(head:  Optional[ListNode]) -> Optional[ListNode]:
            cur_node = None
            nxt_node = head
            while nxt_node is not None:
                tmp = nxt_node.next
                nxt_node.next = cur_node
                cur_node = nxt_node
                nxt_node = tmp
            return cur_node
        
        fst = head
        snd = reversed_ll(mid)

        #O(2 * N/2)
        while snd:
            # now I have 2 lists fst -> [2,4] and snd -> [8,6]
            tmp1, tmp2 = fst.next, snd.next
            fst.next = snd
            snd.next = tmp1
            fst, snd = tmp1, tmp2

            
        

    
            

