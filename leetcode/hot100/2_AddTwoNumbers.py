# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        overflow, l, head = 0, None, None
        while l1 or l2:
            sum = overflow
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            value = sum if sum < 10 else sum % 10
            overflow = int(sum / 10)
            if not l:
                l = ListNode(value)
                head = l
            else:
                l.next = ListNode(value)
                l = l.next
        if overflow != 0:
            l.next = ListNode(overflow)
        return head


if __name__ == "__main__":

    num_2 = ListNode(9)
    num_4 = ListNode(9)
    num_3 = ListNode(9)
    num_2.next = num_4
    num_4.next = num_3
    l1 = num_2

    num_5 = ListNode(9)
    num_6 = ListNode(9)
    num_5.next = num_6
    l2 = num_5

    res = Solution().addTwoNumbers(l1, l2)
    print(res)
