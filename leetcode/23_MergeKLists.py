from typing import List, Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class HeapSort:
    def __init__(self, node_list: List[ListNode]):
        self.node_list = node_list
        self.init_index = len(self.node_list) >> 1
        self.build_min_heap()

    @staticmethod
    def _get_left_index(i):
        return 2 * i

    @staticmethod
    def _get_right_index(i):
        return 2 * i + 1

    def smaller_than(self, ori, smallest):
        ori_val = float("inf") if not ori else ori.val
        smallest_val = float("inf") if not smallest else smallest.val
        return ori_val < smallest_val

    def _min_heapify(self, i: int):
        left, right = self._get_left_index(i), self._get_right_index(i)
        smallest = i
        if left < len(self.node_list) and self.smaller_than(
            self.node_list[left], self.node_list[smallest]
        ):
            smallest = left
        if right < len(self.node_list) and self.smaller_than(
            self.node_list[right], self.node_list[smallest]
        ):
            smallest = right
        if smallest != i:
            self.node_list[i], self.node_list[smallest] = (
                self.node_list[smallest],
                self.node_list[i],
            )
            self._min_heapify(smallest)

    def build_min_heap(self):
        for i in range(len(self.node_list) >> 1, 0, -1):
            self._min_heapify(i)

    def pop(self):
        res = None
        if self.node_list[1] is not None:
            res = self.node_list[1].val
            self.node_list[1] = self.node_list[1].next
            self._min_heapify(1)
        return res


# Solution 1:
# class Solution:
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         head, prev = None, None
#         if not lists:
#             return None
#         nodes = []
#         for li in lists:
#             if li:
#                 nodes.append(li)
#         if not nodes:
#             return None
#         while nodes:
#             min_val, min_index = 9999, 0
#             for index, node in enumerate(nodes):
#                 if min_val > node.val:
#                     min_val, min_index = node.val, index
#             cur_node = nodes[min_index]
#             new_node = ListNode(min_val, None)
#             if not head:
#                 head = new_node
#                 prev = head
#             else:
#                 prev.next = new_node
#                 prev = prev.next
#             if cur_node.next:
#                 nodes[min_index] = nodes[min_index].next
#             else:
#                 nodes.pop(min_index)
#         return head


# Solution 2
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> Optional[ListNode]:
        head, prev = None, None
        if not lists:
            return None
        nodes = [None]
        for li in lists:
            if li:
                nodes.append(li)
        if len(nodes) < 2:
            return None
        heap = HeapSort(nodes)
        while True:
            val = heap.pop()
            if val is None:
                break
            new_node = ListNode(val, None)
            if not head:
                head = new_node
                prev = head
            else:
                prev.next = new_node
                prev = prev.next
        return head


if __name__ == "__main__":
    s = []
    n1 = ListNode(1)
    n2 = ListNode(4)
    n3 = ListNode(5)
    n1.next = n2
    n2.next = n3
    s.append(n1)
    n1 = ListNode(1)
    n2 = ListNode(3)
    n3 = ListNode(4)
    n1.next = n2
    n2.next = n3
    s.append(n1)
    n1 = ListNode(2)
    n2 = ListNode(6)
    n1.next = n2
    s.append(n1)
    res = Solution().mergeKLists(s)
    print(s)
