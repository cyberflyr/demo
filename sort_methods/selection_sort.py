# def selection_sort(A: list):
#     for i in range(len(A)):
#         if i + 1 >= len(A):
#             return A
#         min_index = i
#         for j in range(i + 1, len(A)):
#             if A[j] < A[min_index]:
#                 min_index = j
#         A[i], A[min_index] = A[min_index], A[i]
#     return A


# if __name__ == "__main__":
#     array = [2, 48, 50, 3, 5, 15, 44, 46, 27, 56, 19]
#     res = selection_sort(array)
#     print(res)


# Date: 07/08/2023

def selection_sort(arr: list[int]) -> list[int]:
    for i in range(0, len(arr)-1):
        min_index = i
        # search the min index
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # swap
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

if __name__ == '__main__':
    print(selection_sort([1,3,4,5,9,8,7]))

