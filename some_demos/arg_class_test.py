class Enum1:
    pass


class Enum2:
    pass


class Connector:
    def __init__(self, cls_type):
        self.cls_type = cls_type

    @property
    def connector(self):
        connect_to = None
        if self.cls_type == 'Enum1':
            connect_to = Enum1
        elif self.cls_type == 'Enum2':
            connect_to = Enum2
        return connect_to() if connect_to else None


if __name__ == '__main__':
    val = input('which class?')
    connector = Connector(val).connector
    print(connector)