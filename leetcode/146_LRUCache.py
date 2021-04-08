
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
            if len(self.hash_table)+1 > self.capacity:
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


if __name__ == '__main__':
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
