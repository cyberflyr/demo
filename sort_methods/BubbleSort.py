
def bubble_sort(A: list):
    i = len(A)-1
    j = 0
    while i > 0:
        flag = 1
        while j < i:
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                flag = 0
            j += 1
        if flag:
            break
        j = 0
        i -= 1
    return A


if __name__ == '__main__':
    array = [2, 48, 50, 3, 5, 15, 44, 46, 27, 56, 19]
    res = bubble_sort(array)
    print(res)
