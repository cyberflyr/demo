#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'guozhuangzhi'

import threading


def thread_job():
    print('This is an added Thread, number is %s' % threading.current_thread())


def main():
    added_thread = threading.Thread(target=thread_job)
    # print(threading.active_count())  # 活跃态线程数量
    # print(threading.enumerate())    # 查看活跃线程
    # print(threading.current_thread())   # 当前正在运行的线程
    added_thread.start()
    added_thread.join() # 等待线程结束执行下一条操作


if __name__ == '__main__':
    main()
