
# 自写 —— 存在问题，search和调整没有结合
class InsertSort:
    def __init__(self, u_list: list):
        self.u_list = u_list

    def start_sort(self):
        if len(self.u_list) <= 1:
            return self.u_list
        for i in range(1, len(self.u_list)):
            j = i - 1
            while j >= 0:
                if self.u_list[j] < self.u_list[i]:
                    break
                j -= 1
            current_num = self.u_list[i]
            for index in range(i, j, -1):
                self.u_list[index] = self.u_list[index - 1]
            self.u_list[j+1] = current_num
        return self.u_list


# 书上步骤
def insert_sort(u_list: list):
    if len(u_list) <= 1:
        return u_list
    for i in range(1, len(u_list)):
        key = u_list[i]
        j = i - 1
        while j >= 0 and u_list[j] > key:
            u_list[j + 1] = u_list[j]
            j -= 1
        u_list[j+1] = key
    return u_list


if __name__ == '__main__':
    u_list = [5, 2, 4, 6, 1, 3]
    # print(InsertSort(u_list).start_sort())
    print(insert_sort(u_list))
    # for i in range(5, 3, -1):
    #     print(i)
