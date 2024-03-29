def reverseSecondHalfList(head):
    slow, fast = head, head
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
    pre = slow.next
    cur = pre.next
    while cur:
        pre.next = cur.next
        cur.next = slow.next
        slow.next = cur
        cur = pre.next
    return head
#
# public static ListNode reverseSecondHalfList(ListNode head) {
#     if (head == null || head.next == null)      return head;
#     ListNode fast = head;
#     ListNode slow = head;
#     while (fast.next != null && fast.next.next != null) {
#         fast = fast.next.next;
#         slow = slow.next;
#     }
#     ListNode pre = slow.next;
#     ListNode cur = pre.next;
#     while (cur != null) {
#         pre.next = cur.next;
#         cur.next = slow.next;
#         slow.next = cur;
#         cur = pre.next;
#     }
#     return head;
# }