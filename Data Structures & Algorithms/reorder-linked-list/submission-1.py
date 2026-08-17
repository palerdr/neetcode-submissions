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

        #the slow pointer ends at the back of the front list
        #on an odd number the slow lands st front will have 1 more
        #on an even number the slow lands st the front == back 
        #thus front always has more then the back
        #you also need to sever the slow after you call snd = slow.next
        snd = slow.next
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
        snd = reversed_ll(snd)

        #O(2 * N/2)
        while snd:
            # now I have 2 lists fst -> [2,4,6] and snd -> [10,8,6]
            tmp1, tmp2 = fst.next, snd.next
            fst.next = snd
            snd.next = tmp1
            fst, snd = tmp1, tmp2

            
        

    
            

