import heapq

# heapqpush 支持元组，默认根据元组第一个元素排序


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Item({self.name})"


if __name__ == "__main__":
    q = PriorityQueue()
    q.push(Item("foo"), 1)
    q.push(Item("bar"), 5)
    q.push(Item("hello"), 3)
    print(q.pop())
    print(q._queue)
