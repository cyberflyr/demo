def insertion_sort(l: list):
    print(len(l))
    if len(l) <= 1:
        return l
    for index, value in enumerate(l):
        i = index - 1
        while i >= 0 and value < l[i]:
            l[i + 1] = l[i]
            i -= 1
        l[i + 1] = value
    return l


if __name__ == "__main__":
    source_list = [5, 4, 1, 3, 2]
    res = insertion_sort(source_list)
    print(res)
