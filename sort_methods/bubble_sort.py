# def bubble_sort(A: list):
#     i = len(A) - 1
#     j = 0
#     while i > 0:
#         flag = 1
#         while j < i:
#             if A[j] > A[j + 1]:
#                 A[j], A[j + 1] = A[j + 1], A[j]
#                 flag = 0
#             j += 1
#         if flag:
#             break
#         j = 0
#         i -= 1
#     return A


# if __name__ == "__main__":
#     array = [2, 48, 50, 3, 5, 15, 44, 46, 27, 56, 19]
#     res = bubble_sort(array)
#     print(res)


# Date: 07/08/2023
def bubble_sort(arr :list[int]) -> list[int]:
    if len(arr) < 2:
        return arr
    for i in range(0, len(arr)-1):
        for j in range(len(arr)-2, i-1, -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == '__main__':
    print(bubble_sort([1,3,2,4,7,6,8,9]))
    print(bubble_sort([2,1]))