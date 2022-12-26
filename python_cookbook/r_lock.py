import threading

Lock = threading.Lock()
RLock = threading.RLock()


def a():
    with Lock:
        b()
        c()


def b():
    with Lock:
        c()
        hello()


def c():
    print("c")


def hello():
    print("hello")


if __name__ == "__main__":
    try:
        threading.Thread(target=a, args=()).start()
        threading.Thread(target=b, args=()).start()
    except Exception as e:
        print(e)

    import time

    time.sleep(5)
