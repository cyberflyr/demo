#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "guozhuangzhi"

import threading
from queue import Queue
import datetime


def squ(l, q):
    for i in range(len(l)):
        l[i] = l[i] ** 2
    q.put(l)


def multithreading():
    start_time = datetime.datetime.now()
    q = Queue()
    threads = []
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [2, 2, 2]]
    for i in range(4):
        t = threading.Thread(
            target=squ,
            name=f"job_{i}",
            args=(
                data[i],
                q,
            ),
        )
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    result = []
    for _ in range(4):
        result.append(q.get())
    end_time = datetime.datetime.now()
    print(result)
    print("use time :", end_time - start_time)


def test():
    start_time = datetime.datetime.now()
    datas = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [2, 2, 2]]
    for data in datas:
        for i in range(len(data)):
            data[i] = data[i] ** 2
    end_time = datetime.datetime.now()
    print(datas)
    print("test use time :", end_time - start_time)


if __name__ == "__main__":
    multithreading()
    test()
