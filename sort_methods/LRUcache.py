import collections
import multiprocessing
import threading
import os
import time
import ctypes


def singleton(cls):
    _instance = {}

    def inner(i):
        if not _instance.get(cls):
            _instance[cls] = cls(i)
        return _instance[cls]

    return inner


# @singleton
class LRUCache(object):
    def __init__(self, i):
        self.i = i
        self.mem_pool = collections.deque(maxlen=5)
        self.max_len = 5
        self.obs = {}

    def insert(self, name):
        if self.obs.get(name):
            self.mem_pool.remove(name)
        else:
            if len(self.mem_pool) > self.max_len:
                key = self.mem_pool.pop()
                del self.obs[key]
        for key, val in self.obs.items():
            self.obs[key] += 1
        self.mem_pool.appendleft(name)
        self.obs[name] = 0


def create_cls(i, id_dic, ob_dic):
    time.sleep(i)
    s = LRUCache(i)
    s.insert(i)
    id_dic[i] = id(s)
    ob_dic[i] = s
    print(s)
    print(ob_dic)
    print(s.mem_pool)
    # print(s.mem_pool)
    print(f"{i}: {id(s)} pid:{os.getpid()} {s}")


if __name__ == "__main__":
    # p = multiprocessing.Pool(4)
    id_dic = multiprocessing.Manager().dict()
    ob_dic = multiprocessing.Manager().dict()
    p1 = multiprocessing.Process(target=create_cls, args=(1, id_dic, ob_dic))
    # p1 = threading.Thread(target=create_cls, args=(1,))
    p1.start()
    p2 = multiprocessing.Process(target=create_cls, args=(2, id_dic, ob_dic))
    p2.start()
    p3 = multiprocessing.Process(target=create_cls, args=(4, id_dic, ob_dic))
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    time.sleep(10)
    print(ob_dic)
    print(id(id_dic[1]), id(id_dic[2]), id(id_dic[4]))
    print(id_dic[1] is id_dic[2])
    print(4462135792 is 4462135792)
    # lru2 = LRUCache
    # print(lru2)
    # print(id(lru2))
    # lru.insert(1)
    # print(lru.mem_pool, lru.obs)
    # lru.insert(2)
    # print(lru.mem_pool, lru.obs)
    # lru.insert(1)
    # print(lru.mem_pool, lru.obs)
    # lru.insert(4)
    # print(lru.mem_pool, lru.obs)
    # lru.insert(5)
    # print(lru.mem_pool, lru.obs)
    # lru.insert(1)
    # print(lru.mem_pool, lru.obs)
    # lru.insert(3)
    # print(lru.mem_pool, lru.obs)
    # lru.insert(6)
    # print(lru.mem_pool, lru.obs)
