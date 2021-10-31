
def feb():
    a, b = 0, 1
    yield a
    while True:
        a, b = b, b+a
        yield a


def recursion_feb(a: int, b: int):
    if a < 100:
        print(a)
        recursion_feb(b, a+b)


if __name__ == '__main__':
    for i in feb():
        if i > 100:
            break
        print(i)
    # recursion_feb(0, 1)