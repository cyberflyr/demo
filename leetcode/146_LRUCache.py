from dataclasses import dataclass
from typing import Optional, Tuple

# Solution 1

# class ListNode:
#     def __init__(
#             self,
#             key: int = 0,
#             val: int = 0,
#             prev: Optional['ListNode'] = None,
#             next: Optional['ListNode'] = None
#     ):
#         self.key = key
#         self.val = val
#         self.prev = prev
#         self.next = next
#
#
# class CycleList:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.length = 0
#         self.head = None
#         self.tail = None
#
#     def move_to_tail(self, node: ListNode) -> None:
#         if self.tail is node:
#             return
#         if self.head is node:
#             self.head = self.head.next
#
#         # 互换相邻位置
#         if node.prev:
#             node.prev.next = node.next
#         if node.next:
#             node.next.prev = node.prev
#
#         node.next = None
#         node.prev = self.tail
#         self.tail.next = node
#         self.tail = node
#
#     def put_to_tail(self, key: int, val: int) -> Tuple[Optional[int], ListNode]:
#         if not self.head:
#             self.head = ListNode(key, val)
#             self.tail = self.head
#             self.length += 1
#             return None, self.head
#         else:
#             node = ListNode(key, val, prev=self.tail, next=None)
#             self.tail.next = node
#             self.tail = node
#             self.length += 1
#             if self.length > self.capacity:
#                 del_key = self.head.key
#                 self.head = self.head.next
#                 self.length -= 1
#                 return del_key, node
#             return None, node
#
#
# @dataclass
# class MapItem:
#     val: int
#     node: ListNode
#
#
# class LRUCache:
#     def __init__(self, capacity: int):
#         self.cycle_list = CycleList(capacity)
#         self.hashmap = {}
#
#     def get(self, key: int) -> int:
#         map_item = self.hashmap.get(key)
#         if map_item:
#             self.cycle_list.move_to_tail(map_item.node)
#             return map_item.val
#         else:
#             return -1
#
#     def put(self, key: int, value: int) -> None:
#         map_item = self.hashmap.get(key)
#         if map_item:
#             if map_item.val != value:
#                 map_item.val = value
#                 map_item.node.val = value
#             self.cycle_list.move_to_tail(map_item.node)
#         else:
#             del_key, node = self.cycle_list.put_to_tail(key, value)
#             if del_key is not None:
#                 self.hashmap.pop(del_key, None)
#             self.hashmap[key] = MapItem(value, node)

# Solution 2
class LRUCache:
    def __init__(self, capacity: int):
        self.hash_table = dict()
        self.capacity = capacity
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        node = self.hash_table.get(key)
        if not node:
            return -1
        if len(self.hash_table) > 1:
            self.append_node_to_tail(node, already_exists=True)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.hash_table.get(key)
        if node:
            node.value = value
            self.append_node_to_tail(node, already_exists=True)
        else:
            node = Node(key, value)
            self.append_node_to_tail(node, already_exists=False)
        self.hash_table[key] = node

    def append_node_to_tail(self, node, already_exists=False):
        if not self.head:
            self.head = node
            self.tail = node
            return
        if already_exists:
            if not node.next_node:
                # 说明是最后一个节点, 不做操作
                return
            if not node.prev_node:
                # 说明是第一个节点，向后置一个节点，prev_node还是
                if node.next_node:
                    node.next_node.prev_node = None
                    self.head = node.next_node
            # 在中间的情况
            if node.prev_node:
                node.prev_node.next_node = node.next_node
            if node.next_node:
                node.next_node.prev_node = node.prev_node
        else:
            if len(self.hash_table) + 1 > self.capacity:
                del self.hash_table[self.head.key]
                if self.head.next_node:
                    self.head.next_node.prev_node = None
                    self.head = self.head.next_node
                else:
                    self.head = node
                    self.tail = node
                    return
        self.tail.next_node = node
        node.prev_node = self.tail
        node.next_node = None
        self.tail = node


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev_node = None
        self.next_node = None


if __name__ == "__main__":
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    print(lru.get(1))
    lru.put(3, 3)
    print(lru.get(2))
    lru.put(4, 4)
    print(lru.get(1))
    print(lru.get(3))
    print(lru.get(4))
