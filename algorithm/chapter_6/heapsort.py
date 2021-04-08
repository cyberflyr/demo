
def left(i):
    return i << 1


def right(i):
    return (i << 1) + 1


def max_heapify(l: list, i):
    if i <= 0:
        return
    left_index = left(i)
    right_index = right(i)
    if left_index < len(l) and l[left_index] > l[i]:
        largest = left_index
    else:
        largest = i
    if right_index < len(l) and l[right_index] > l[largest]:
        largest = right_index
    if largest != i:
        l[largest], l[i] = l[i], l[largest]
        max_heapify(l, largest)


def min_heapify(l: list, i):
    if i <= 0:
        return
    left_index = left(i)
    right_index = right(i)
    if left_index < len(l) and l[left_index] < l[i]:
        smallest = left_index
    else:
        smallest = i
    if right_index < len(l) and l[right_index] < l[smallest]:
        smallest = right_index
    if smallest != i:
        l[smallest], l[i] = l[i], l[smallest]
        min_heapify(l, smallest)


if __name__ == '__main__':
    l = [None, 27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
    max_heap, min_heap = l[:], l[:]
    for i in range(int(len(l)/2), 0, -1):
        max_heapify(max_heap, i)
    for i in range(int(len(l)/2), 0, -1):
        min_heapify(min_heap, i)
    print(l)
    print(max_heap)
    print(min_heap)