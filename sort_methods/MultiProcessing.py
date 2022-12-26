#!/usr/bin/env python
# -*- coding: utf-8 -*-
import multiprocessing


def add(i, a):
    while True:
        a += i


def multiprocessing_build():
    # start_time = datetime.datetime.now()
    p = multiprocessing.Pool(4)
    for i in range(4):
        a = 0
        p.apply_async(add, args=(i, a))
    print("Waiting for all subprocess done...")
    p.close()
    p.join()
    # end_time = datetime.datetime.now()
    # print(f"Multithreading finished in {end_time - start_time}")


if __name__ == "__main__":
    multiprocessing_build()
