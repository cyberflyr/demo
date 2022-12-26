class Singleton:
    def __init__(self, cls):
        self.cls = cls
        self._instance = {}
        print("__init__")

    def __call__(self, *args, **kwargs):
        print("__call__")
        if self.cls not in self._instance:
            self._instance[self.cls] = self.cls(*args, **kwargs)
        return self._instance[self.cls]


@Singleton
class A:
    def __init__(self, name="gzz"):
        print("%s" % name)
        print(self.__class__.__name__)


if __name__ == "__main__":
    pass
    a = A()
    b = A()
    # print(id(a))
    # print(id(b))
    # print(a is b)
