

if __name__ == '__main__':
    # A = [1, 2]
    # # for item in A:
    # #     print(id(item))
    # # b = 1
    # # print(id(b))
    # B = lambda A: [x**2 for x in A]
    # print(B(A))
    # y = {x**2 for x in range(4)}
    # print(y)
    # print(type(y))
    s = 'hellooo\n'
    new_str = ''
    last_c = None
    times = 0
    for c in s:
        if c != last_c:
            if times <= 1:
                if last_c is not None:
                    new_str += last_c
            else:
                new_str += f"/{times}{last_c}"
            last_c = c
            times = 1
        else:
            times += 1
    # #   结尾处理
    # if times == 1:
    #     new_str += f"{last_c}"
    # else:
    #     new_str += f"/{times}{last_c}"
    print(new_str)