#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'guozhuangzhi'


class Student:
    def __init__(self, name, number, age):
        self.name = name
        self._number = number
        self.__age = age
    area = 'BeiJing'
    _distrinct = 'ChangPing'
    __ID = 123


if __name__ == '__main__':
    gzz = Student("gzz", 1, 22)
    print(gzz.name, gzz._number, gzz._Student__age)
