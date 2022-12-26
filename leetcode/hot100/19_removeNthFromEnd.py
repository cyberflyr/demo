class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        null_head = ListNode(0, next=head)
        walker, slow, pre_slow = head, head, null_head

        while walker:
            if n <= 0:
                pre_slow = pre_slow.next
                slow = slow.next
            n -= 1
            walker = walker.next
        pre_slow.next = slow.next

        return null_head.next
