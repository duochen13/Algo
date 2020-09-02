
// Input: 1->2->3->4->5->NULL
// Output: 5->4->3->2->1->NULL

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}


// let cur_ptr = head;             
// let pre_ptr = null;
// while (cur_ptr !== null) {
//     let temp = cur_ptr.next;    2            3              4
//     cur_ptr.next = pre_ptr;     1->null      2->(1->null)   3->(2->1->null)
//     pre_ptr = cur_ptr;          pre = 1      2              3
//     cur_ptr = temp;             cur = 2      3              4
// }
// return pre_ptr

public class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode preNode = null;
        ListNode curNode = head;
        while (curNode != null) {
            ListNode tmp = curNode.next;
            curNode.next = preNode;
            preNode = curNode;
            curNode = tmp;
        }
        return preNode;
    }
    public static void main(String[] args) {
        System.out.println("hello wolrd");
    }
}

// cur  tmp
// (1)->(2->3->4->5->NULL)
//  ^
// (2 -> 1) -> (3 4 5 null)
//       ^     
// (3 -> 2 -> 1) -> 4 5 null
//            ^ 
// (4 -> 3 -> 2 -> 1) -> 5 null
// 
