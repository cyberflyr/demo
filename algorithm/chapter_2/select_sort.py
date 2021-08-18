def select_sort(l: list):
    if len(l) < 2:
        return l
    for i in range(len(l)-1):
        max_pos = i
        j = i + 1
        if j < len(l):
            while j < len(l):
                if l[j] > l[max_pos]:
                    max_pos = j
                j += 1
        l[i], l[max_pos] = l[max_pos], l[i]
    return l

if __name__ == '__main__':
    u_list = [5, 2, 4, 6, 1, 3]
    # print(InsertSort(u_list).start_sort())
    print(select_sort(u_list[:]))
