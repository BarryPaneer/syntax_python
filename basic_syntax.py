# -*- coding: utf-8 -*-
"""
    Python Env:     python3
    Briet:          test basic syntax of python3
    Author:         Barry
"""
import unittest


class TestTypeFunction(unittest.TestCase):
    """Usage: how to create a class by type()"""
    def test_type_func(self):
        class BaseClass(object):
            def echo_a(self):
                print("call TestTypeFunction.echo_a()")
                return True

        def echo_my_class(self):
            print("call TestTypeFunction.echo_my_class()")
            return True

        my_class_type = type('MyClass', (BaseClass, ), {'echo_my_class': echo_my_class})
        my_class = my_class_type()
        self.assertNotEqual(my_class_type.mro(), None)
        self.assertNotEqual(my_class, None)
        self.assertEqual(my_class.echo_a(), True)
        self.assertEqual(my_class.echo_my_class(), True)


class TestClassSyntax(unittest.TestCase):
    """Usage: derive a new class from base class which hasn't a __init__()"""
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
        self.assertNotEqual(id(obj), None)


class TestMetaClassSyntax(unittest.TestCase):
    """Usage: how to create a metaclass which support singleton trait"""
    def test_meta_class(self):
        class MyMetaClass(type):
            def __new__(mcs, name, bases, attrs):
                """allocate memory operation / create an EarthIsSingleton class"""
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
                super().__init__(name, bases, attrs)
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
                self.AAA = 1000
                print("enter Earth.__init__() ...")

        earth1 = EarthIsSingleton()
        earth2 = EarthIsSingleton()
        self.assertEqual(id(earth1), id(earth2))
        #self.assertEqual(earth1.AAA, 1000)


def __main():
    unittest.main()


if __name__ == '__main__':
    __main()

