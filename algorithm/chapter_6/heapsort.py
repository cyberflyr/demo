def get_left_child(i):
    return 2 * i


def get_right_child(i):
    return 2 * i + 1


def max_heapify(l: list, i: int):
    left, right = get_left_child(i), get_right_child(i)  # index of left, right child
    largest = i
    if left < len(l) and l[left] > l[i]:
        largest = left
    if right < len(l) and l[right] > l[largest]:
        largest = right
    if largest != i:
        l[i], l[largest] = l[largest], l[i]
        max_heapify(l, largest)  # largest is the origin index of max num


def build_max_heap(l: list):
    for i in range(len(l) >> 1, 0, -1):
        max_heapify(l, i)


if __name__ == "__main__":
    s = [None, 27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
    build_max_heap(s)
    print(s)
