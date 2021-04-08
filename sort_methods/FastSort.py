
def fast_sort(A: list, left: int, right: int):
    print(A, left, right)
    if left >= right:
        return
    value = A[left]
    left_flag = left
    right_flag = right
    while left < right:
        while A[right] >= value and left < right:
            right -= 1
        A[left] = A[right]
        while A[left] < value and left < right:
            left += 1
        A[right] = A[left]
    A[left] = value
    fastSort(A, left_flag, left-1)
    fastSort(A, left+1, right_flag)
    return A


if __name__ == '__main__':
    array = [2, 48, 50, 3, 5, 15, 44, 46, 27, 56, 19]
    res = fast_sort(array, 0, len(array)-1)
