from typing import List


def find_closest_num(nums: List, target: int) -> int:
    start = 0
    end = len(nums) - 1
    min_distance, min_index = float("inf"), float("inf")
    while start <= end:
        equal = False
        mid = (start + end) >> 1
        if nums[mid] < target:
            start = mid + 1
        elif nums[mid] > target:
            end = mid - 1
        else:
            equal = True
        while mid > 0 and nums[mid] == nums[mid - 1]:
            mid -= 1
        if equal:
            return mid
        distance = abs(nums[mid] - target)
        if distance < min_distance:
            min_distance = distance
            min_index = mid

    return min_index


if __name__ == "__main__":
    # nums = [1, 2, 2, 3, 4, 4, 5]  # target = 4
    nums = [1, 2, 2, 3, 4, 4, 5]  # target = 5
    # nums = [0, 0, 0, 0, 1]
    print(find_closest_num(nums, 5))
