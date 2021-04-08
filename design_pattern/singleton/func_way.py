
def singleton(cls):
    _instance = {}

    def inner():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]
    return inner


@singleton
class Single:
    def __init__(self):
        self.x = 'guozhuangzhi'


if __name__ == '__main__':
    cls1 = singleton

    print(cls1 is cls2)
