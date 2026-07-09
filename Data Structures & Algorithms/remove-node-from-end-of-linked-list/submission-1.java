/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if(head == null){return head;}
        //if empty hust return the head
        ListNode curr = head;
        int k = 1;
        while (curr.next!=null){
            curr = curr.next;
            k++;
        } //gives us the size of the list

        if ( k == n){
            return head.next;
        }

        ListNode c = head;
        int s = k - n - 1;
        for (int i = 0; i < s; i++) {
           c = c.next;
        }
        c.next = c.next.next;
        
        return head;
        }

    }

