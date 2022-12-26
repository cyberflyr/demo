class share_arg:
    share_list = list()

    def __init__(self, name):
        self.name = name

    def add_name(self, name):
        self.share_list.append(name)


if __name__ == "__main__":
    a = share_arg("dog")
    b = share_arg("cat")
    a.add_name("dog")
    b.add_name("cat")
    print(a.share_list)
