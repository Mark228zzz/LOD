class MyMeta(type):
    def __new__(cls, *args, **kwargs):
        print('gg')


class C(metaclass=MyMeta):
    pass


c = C()
