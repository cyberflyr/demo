# 书上步骤
# def insert_sort(l: list):
#     if len(l) < 2:
#         return l
#     for i in range(1, len(l)):
#         num = l[i]
#         j = i - 1
#         while j >= 0 and num < l[j]:
#             l[j+1] = l[j]
#             j -= 1
#         l[j+1] = num
#     return l

# insert sort asc
def insert_sort_asc(l: list):
    if len(l) < 2:
        return l
    for i in range(1, len(l), 1):
        val = l[i]
        j = i - 1
        while j >= 0 and l[j] > val:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = val
    return l


# insert sort desc
def insert_sort_desc(l: list):
    if len(l) < 2:
        return l
    for i in range(1, len(l), 1):
        val = l[i]
        j = i - 1
        while j >= 0 and l[j] < val:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = val
    return l


if __name__ == "__main__":
    u_list = [5, 2, 4, 6, 1, 3]
    # print(InsertSort(u_list).start_sort())
    print(insert_sort_asc(u_list[:]))
    print(insert_sort_desc(u_list[:]))

    # for i in range(5, 3, -1):
    #     print(i)
