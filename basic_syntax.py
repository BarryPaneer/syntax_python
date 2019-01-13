# -*- coding: utf-8 -*-
"""
    Python Env:     python3
    Briet:          test basic syntax of python3
    Author:         Barry
"""
import unittest


class TestTypeFunction(unittest.TestCase):
    """test 'type()' function, how to create a class by type()"""
    def test_type_func(self):
        class A(object):
            def echo_a(self):
                print("echo A")
                return True

        def echo_my_class(self):
            print("echo MyClass")
            return True

        my_class = type('my_class', (A, ), {'echo_my_class': echo_my_class})
        print(dir(my_class))
        self.assertNotEqual(my_class, None)
        self.assertNotEqual(my_class.mro(), None)
        #self.assertEqual(my_class.echo_a(), True)
        #self.assertEqual(my_class.echo_my_class(), True)


class TestClassSyntax(unittest.TestCase):
    def test_class(self):
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
        print(id(obj))
        self.assertNotEqual(id(obj), None)


def meta_func(name, bases, attrs):
    """allocate memory operation"""
    print("enter MyMetaClass.__new__()")
    set_attrs = ((name, value) for name, value in attrs.items() if not name.startswith('__'))
    uppercase_attr = dict((name.upper(), value) for name, value in set_attrs)
    return type(name, bases, uppercase_attr)


class MyMetaClass(type):
    def __new__(mcs, name, bases, attrs):
        """allocate memory operation"""
        print("enter MyMetaClass.__new__()")
        if name == "Model":
            return super().__new__(mcs, name, bases, attrs)
        else:
            set_attrs = ((name, value) for name, value in attrs.items() if not name.startswith('__'))
            uppercase_attr = dict((name.upper(), value) for name, value in set_attrs)
            return super().__new__(mcs, name, bases, uppercase_attr)

    def __init__(cls, name, bases, attrs):
        """enter MyMetaClass.__init__()"""
        print("enter MyMetaClass.__init__()")
        super().__init__(name,bases,attrs)
        cls.__instance = None

    def __call__(cls, *args, **kargs):
        """enter MyMetaClass.__call__()"""
        print("enter MyMetaClass.__call__()")
        if cls.__instance:
            return cls.__instance
        else:
            cls._instance = super().__call__(*args, **kargs)
            return cls.__instance


class EarthIsSingleton(metaclass=MyMetaClass):
    People = "abc"
    __instance = None

    def __init__(self):
        self.AAA = 1
        print("enter Earth.__init__() ...")


class TestMetaClassSyntax(unittest.TestCase):
    def test_meta_class(self):
        """ test __metaclass__ __new__ __init__ __call__ """
        earth1 = EarthIsSingleton()
        earth2 = EarthIsSingleton()
        self.assertEqual(id(earth1), id(earth2))


def __main():
    unittest.main()


if __name__ == '__main__':
    __main()

