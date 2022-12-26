input = [5, 7, 9, 8, 6, 3, 5]


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    if len(arr) == 2:
        if arr[0] > arr[1]:
            arr.sort(reverse=True)
        return arr
    return merge_sort([])
