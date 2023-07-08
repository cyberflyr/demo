# def insertion_sort(l: list):
#     print(len(l))
#     if len(l) <= 1:
#         return l
#     for index, value in enumerate(l):
#         i = index - 1
#         while i >= 0 and value < l[i]:
#             l[i + 1] = l[i]
#             i -= 1
#         l[i + 1] = value
#     return l


# if __name__ == "__main__":
#     source_list = [5, 4, 1, 3, 2]
#     res = insertion_sort(source_list)
#     print(res)


# Date: 07/08/2023

def insertion_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    for i in range(1, len(arr)):
        num = arr[i]
        j = i - 1
        while j >=0 and arr[j] > num:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = num
    return arr

if __name__ == '__main__':
    print(insertion_sort([1,3,2,4,7,6,8,9]))
    print(insertion_sort([2,1]))
