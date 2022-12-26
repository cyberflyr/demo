from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        null_head = ListNode(0)
        null_head.next = head
        slow = null_head
        walker = head
        while walker:
            if walker.next:
                walker = walker.next.next
            else:
                walker = walker.next
            slow = slow.next
            if walker is slow:
                return True

        return False
