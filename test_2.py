import dis


def func_a():
    a = list()
    return a


def func_b():
    b = []
    return b
# print(dis.dis("{}"))
# print(dis.dis("dict()"))
print(dis.dis(func_a))
print(dis.dis(func_b))