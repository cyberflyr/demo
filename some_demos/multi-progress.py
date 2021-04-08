#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'guozhuangzhi'

import os
import datetime
print(f"Process {os.getpid()} start ...")

pid = os.fork()
if pid == 0:
    pid1 = os.fork()
    if pid1 == 0:
        print('I am child process (%s) and my parent is %s. Time is %s' % (os.getpid(), os.getppid(), datetime.datetime.now()))
    else:
        print('I (%s) just created a child process (%s). Time is %s' % (os.getpid(), pid1, datetime.datetime.now()))
    print('I am child process (%s) and my parent is %s. Time is %s' % (os.getpid(), os.getppid(), datetime.datetime.now()))
else:
    print('I (%s) just created a child process (%s). Time is %s' % (os.getpid(), pid, datetime.datetime.now()))


a={"a":[]}
def block():
    # 一个 block 函数
    pass

def abc():
    if len(a['a'])==0:
        block()
        a['a'].append(2)

def abc2():
    if len(a['a'])==0:
        block()
        a['a'].append(3)

print(a['a'])
