#!/usr/bin/env python
# -*- coding: utf-8 -*-


def gen():
    for x in range(3):
        yield x
    yield 4

if __name__ == '__main__':
    # gene = gen()
    # print(gene.__next__())
    # print(gene.__next__())
    # print(gene.__next__())
    # gene.__iter__().send(5)
    # print(gene.__next__())
    # print(gene.__next__())

    # l = [1, 2, 3]
    # l = l.__iter__()
    # print(next(l))
    # print(next(l))
    # print(next(l))

    def func():
        x = 1
        while True:
            y = (yield x)
            x += y


    geniter = func()
    print(geniter.__next__())  # 1
    print(geniter.__next__())
    print(geniter.send(3))  # 4
    print(geniter.send(10))  # 14
