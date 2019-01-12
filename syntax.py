# -*- coding: utf-8 -*-


def test_type_func():
    class A(object):
        def echo_a(self):
            print("echo A")

    def echo_my_class(self):
            print("echo MyClass")

    my_class = type('my_class', (A, ), {'echo_my_class':echo_my_class})

    obj = my_class()
    print(my_class.__mro__)
    print(my_class.mro())
    obj.echo_a()
    obj.echo_my_class()


def test_class():
    class Base:
        pass

    class A(Base):
        def __init__(self, x):
            super().__init__()
            print('print A.__init__()', x)

    class B(A):
        def __init__(self):
            print('print B.__init__')
            super().__init__("input x")

    obj = B()
    print(obj)


def test_meta_class():
    class my_metaclass(type):
        def __new__(cls, name, bases, attrs):
            """allocate memory operation"""
            if name == "Model":
                return super().__new__(cls, name, bases, attrs)
            else:
                set_attrs = ((name, value) for name, value in dct.items() if not name.startswith('__'))
                uppercase_attr = dict((name.upper(), value) for name, value in set_attrs)
                return super().__new__(cls, name, bases, uppercase_attr)

        def __init__(cls, name, bases, attrs):
            """xxx"""
            super().__init__(name,bases,attrs)
            cls.__instance = None

        def __call__(self, *args, **kargs):
            """xxx"""
            if self._instance:
                return self.__instance
            else:
                self._instance = super().__call__(*args, **kargs)
                return self.__instance

    class Earth(object):
        __metaclass__ = my_metaclass

        def __init__(self):
            pass

        def echo(self):
            print("ok...")

    obj = Earth()
    obj.echo()


def __main():
    print("begin.................")
    test_type_func()
    test_class()
    test_meta_class()
    print("done..................")


if __name__ == '__main__':
    __main()

