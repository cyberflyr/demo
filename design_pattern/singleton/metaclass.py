

class Singleton(type):

    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            s = super(Singleton, cls)
            cls._instance[cls] = super().__call__(cls, *args, **kwargs)
        return cls._instance[cls]


class A(metaclass=Singleton):
    def __init__(self):
        pass


if __name__ == '__main__':
    a = A()
    b = A()
    print(a is b)
    args = ()
    kwargs = {}
    s = type.__call__(*args, **kwargs)
    print(s)
