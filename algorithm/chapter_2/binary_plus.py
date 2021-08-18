
def binary_plus(l1: list, l2: list):
    # l1, l2 each bit of binary num , from low to high position
    if not l1 or not l2:
        return
    l1_pos = 0
    l2_pos = 0
    overflow = 0
    l3 = []
    while l1_pos < len(l1) or l2_pos < len(l2):
        res_of_sum = overflow
        if l1_pos < len(l1):
            res_of_sum += l1[l1_pos]
            l1_pos += 1
        if l2_pos < len(l2):
            res_of_sum += l2[l2_pos]
            l2_pos += 1
        res_left = res_of_sum % 2
        l3.append(res_left)
        overflow = 1 if res_of_sum >= 2 else 0
    if overflow:
        l3.append(overflow)
    return l3

if __name__ == '__main__':
    l1 = [1,1,1]
    l2 = [0,0,1]
    print(binary_plus(l1, l2))