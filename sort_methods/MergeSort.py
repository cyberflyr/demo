def merge_sort(arr: list, left: int, right: int):
    if left < right:
        mid = int((left + right) / 2)
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        return merge(arr, left, mid, right)
    return arr


def merge(arr, left, mid, right):
    temp_arr = []
    i = left
    j = mid + 1
    while i <= mid and j <= right:
        if arr[i] < arr[j]:
            temp_arr.append(arr[i])
            i += 1
        else:
            temp_arr.append(arr[j])
            j += 1
    while i <= mid:
        temp_arr.append(arr[i])
        i += 1
    while j <= right:
        j += 1
    return temp_arr


if __name__ == "__main__":
    array = [2, 48, 50, 3, 5, 15, 44, 46, 27, 56, 19]
    res = merge_sort(array, 0, len(array) - 1)
    print(res)
