def singleton(cls):
    __instance = {}

    def inner(*args, **kwargs):
        if cls not in __instance:
            __instance[cls] = cls(*args, **kwargs)
        return __instance[cls]

    return inner


@singleton
class Queue:
    def __init__(self, input: list):
        self.queue = input

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        return self.queue.pop(0)

    def show_queue(self):
        print(self.queue)


if __name__ == "__main__":
    queue = Queue([123])
    print(id(queue))
    queue = Queue([123])
    print(id(queue))
    # for item in [1, 2, 3, 4, 5]:
    #     queue.push(item)
    # queue.show_queue()
    # for _ in range(5):
    #     print(queue.pop())
    # queue.show_queue()
