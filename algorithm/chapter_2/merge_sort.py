
class MergeSort:
    def __init__(self, u_list):
        self.u_list = u_list

    def merge_sort(self, start, stop):
        if start < stop:
            mid = int((start+stop)/2)
            self.merge_sort(start, mid)
            self.merge_sort(mid+1, stop)
            self.merge(start, mid, stop)
        return self.u_list

    # 自写
    # def merge(self, start, mid, stop):
    #     list_a = self.u_list[start:mid+1]
    #     list_b = self.u_list[mid+1:stop+1]
    #     i, j = 0, 0
    #     k = start
    #     while i <= len(list_a)-1 and j <= len(list_b)-1:
    #         if list_a[i] < list_b[j]:
    #             self.u_list[k] = list_a[i]
    #             i += 1
    #         else:
    #             self.u_list[k] = list_b[j]
    #             j += 1
    #         k += 1
    #     while i <= len(list_a)-1:
    #         self.u_list[k] = list_a[i]
    #         k += 1
    #         i += 1
    #     while j <= len(list_b)-1:
    #         self.u_list[k] = list_b[j]
    #         k += 1
    #         j += 1

    # 书上append inf作为哨兵
    def merge(self, start, mid, stop):
        list_a = self.u_list[start:mid+1]
        list_b = self.u_list[mid+1:stop+1]
        list_a.append(float('inf'))
        list_b.append(float('inf'))
        i, j = 0, 0
        k = start
        while k <= stop:
            if list_a[i] < list_b[j]:
                self.u_list[k] = list_a[i]
                i += 1
            else:
                self.u_list[k] = list_b[j]
                j += 1
            k += 1


if __name__ == '__main__':
    u_list = [2, 4, 5, 7, 1, 2, 3, 6, 9]
    print(MergeSort(u_list).merge_sort(0, len(u_list)-1))