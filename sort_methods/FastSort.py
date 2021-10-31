
# def fast_sort(A: list, left: int, right: int):
#     if left >= right:
#         return
#     value = A[left]
#     left_flag = left
#     right_flag = right
#     while left < right:
#         while A[right] >= value and left < right:
#             right -= 1
#         A[left] = A[right]
#         while A[left] < value and left < right:
#             left += 1
#         A[right] = A[left]
#     A[left] = value
#     fast_sort(A, left_flag, left-1)
#     fast_sort(A, left+1, right_flag)
#     return A
# def partition(A, low, high):
#     val = A[high]
#     i = low - 1
#     j = low
#     while j < high:
#         if A[j] <= val:
#             i += 1
#             A[i], A[j] = A[j], A[i]
#         j += 1
#     A[i+1], A[j] = A[j], A[i+1]
#     return i + 1

#
# def fast_sort(A: list, left: int, right: int):
#     if left < right:
#         p = partition(A, left, right)
#         fast_sort(A, left, p-1)
#         fast_sort(A, p+1, right)


def partition(array, left, right):
    flag_num = array[right]
    pos = left - 1
    walker = left
    while walker < right:
        if array[walker] <= flag_num:
            pos += 1
            array[pos], array[walker] = array[walker], array[pos]
        walker += 1
    array[pos+1], array[right] = array[right], array[pos+1]
    return pos + 1


def fast_sort(array, left, right):
    if left > right:
        mid = partition(array, left, right)
        fast_sort(array, left, mid-1)
        fast_sort(array, mid+1, right)


if __name__ == '__main__':
    array = [2, 48, 50, 3, 5, 15, 44, 46, 27, 56, 19]
    res = fast_sort(array, 0, len(array)-1)
    print(array)
