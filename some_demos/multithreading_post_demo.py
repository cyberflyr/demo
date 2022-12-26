#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "guozhuangzhi"

import os, requests, threading, datetime
import multiprocessing
from queue import Queue

IMAGE_LIST = [f"https://www.baidu.com"]


def get_icon_multi(i, hello):
    start_time = datetime.datetime.now()
    print(f"job_{i} start time :{start_time}")
    image_folder = os.path.abspath(os.path.dirname(__file__))
    r = requests.get(IMAGE_LIST[i])
    print("request use:", datetime.datetime.now() - start_time)
    # print(r.content)
    with open(f"{image_folder}/icon_{i}.png", "wb") as f:
        f.write(r.content)


def get_icon_normal():
    start_time = datetime.datetime.now()
    image_folder = os.path.abspath(os.path.dirname(__file__))
    for i in range(len(IMAGE_LIST)):
        r = requests.get(IMAGE_LIST[i])
        print("request use:", datetime.datetime.now() - start_time)
        print(r.content)
        with open(f"{image_folder}/icon_{i+100}.jpg", "wb") as f:
            f.write(r.content)
    end_time = datetime.datetime.now()
    print(f"Normal finished in {end_time-start_time}")


def multithreading_build():
    q = Queue(3)
    start_time = datetime.datetime.now()
    threads = []
    for i in range(len(IMAGE_LIST)):
        t = threading.Thread(target=get_icon_multi, args=(i, "hi"))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    end_time = datetime.datetime.now()
    print(f"Multithreading finished in {end_time - start_time}")


def multiProcessing_build():
    start_time = datetime.datetime.now()
    p = multiprocessing.Pool(4)
    for i in range(len(IMAGE_LIST)):
        p.apply_async(get_icon_multi, args=(i,))
    print("Waiting for all subprocess done...")
    p.close()
    p.join()
    end_time = datetime.datetime.now()
    print(f"Multithreading finished in {end_time - start_time}")


if __name__ == "__main__":
    # get_icon_normal()
    # multithreading_build()
    multiProcessing_build()
    # print(IMAGE_LIST[0])
    # r = requests.get(IMAGE_LIST[0])
    # print(r.content)
    # start_time = datetime.datetime.now()
    # r = requests.get(IMAGE_LIST[0])
    # time = datetime.datetime.now()
    # print(r.content)
    # print('request use:', datetime.datetime.now() - start_time)
    # print('print time:', time - start_time)
