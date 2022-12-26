def find_max_crossing_subarray(array, low, middle, high):
    left_sum = float("-inf")
    sum = 0
    max_left, max_right = middle, middle
    for i in range(middle, low - 1, -1):
        sum += array[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = float("-inf")
    sum = 0
    for i in range(middle + 1, high + 1, 1):
        sum += array[i]
        if sum > right_sum:
            right_sum = sum
            max_right = i
    return max_left, max_right, left_sum + right_sum


def find_max_subarray(array, low, high):
    if low == high:
        return low, high, array[low]
    elif low + 1 == high:
        max_sum = max(array[low], array[high], array[low] + array[high])
        if max_sum == array[low]:
            return low, low, array[low]
        elif max_sum == array[high]:
            return high, high, array[high]
        else:
            return low, high, array[low] + array[high]
    else:
        mid = int((low + high) / 2)
        left_low, left_high, left_sum = find_max_subarray(array, low, mid)
        right_low, right_high, right_sum = find_max_subarray(array, mid, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(
            array, low, mid, high
        )
        max_sum = max(left_sum, right_sum, cross_sum)
        if max_sum == left_sum:
            return left_low, left_high, left_sum
        elif max_sum == right_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


if __name__ == "__main__":
    array = [5, 4, -1, 7, 8]
    print(find_max_crossing_subarray(array, 0, 2, 4))
    print(find_max_subarray(array, 0, len(array) - 1))
