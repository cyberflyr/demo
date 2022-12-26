def selection_sort(A: list):
    for i in range(len(A)):
        if i + 1 >= len(A):
            return A
        min_index = i
        for j in range(i + 1, len(A)):
            if A[j] < A[min_index]:
                min_index = j
        A[i], A[min_index] = A[min_index], A[i]
    return A


if __name__ == "__main__":
    array = [2, 48, 50, 3, 5, 15, 44, 46, 27, 56, 19]
    res = selection_sort(array)
    print(res)
