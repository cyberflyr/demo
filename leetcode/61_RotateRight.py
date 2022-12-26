from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        walker = head
        length = 1
        while walker.next:
            length += 1
            walker = walker.next
        walker.next = head

        k = k % length
        j = length - k
        while j > 0:
            head = head.next
            walker = walker.next
            j -= 1
        walker.next = None
        return head
