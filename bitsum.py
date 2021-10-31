
def bit_sum(a: list, b: list):
    i = 0
    overflow = 0
    res = []
    while i < len(a) and i < len(b):
        res.append(a[i]^b[i])
        overflow =
