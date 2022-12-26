def bin_search(l: list, target):
    # l: asc sorted list
    pos = -1
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) >> 1
        if l[mid] > target:
            high = mid - 1
        elif l[mid] < target:
            low = mid + 1
        else:
            return mid
    return pos


if __name__ == "__main__":
    u_list = [0, 1, 2, 3, 4, 5]
    print(bin_search(u_list, 4))
