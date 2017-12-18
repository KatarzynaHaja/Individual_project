import sys
import importlib.util
from inspect import isclass

class Foo:
    def __init__(self):
        spec = importlib.util.spec_from_file_location("test_package.tests","C:\\Users\\Kasior\PycharmProjects\Individual_project\\test_package\\tests.py")
        foo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(foo)

        self.classes = [x for x in dir("tests") if isclass(getattr("tests", x))]


f = Foo()