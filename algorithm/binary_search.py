from typing import List

def binary_search(arr: List[int], target: int) -> int:
    start, end = 0, len(arr)-1
    while start < end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return arr[start] if arr[start] == target else -1


if __name__ == '__main__':
    print(binary_search([1,2,3,5,7,9], 8))
