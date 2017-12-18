import unittest
#from test_package import tests  #problem z tym importem !!!!!!
from inspect import isclass
#import test_package.tests
import importlib
import sys
import inspect
import re

class Get_result_of_tests:
    def __init__(self, filename,package):
        self.module = package+'.'+filename
        self.mod = importlib.import_module(self.module)
        self.filename = filename
        self.package = package
        self.classes = list()
        for name, obj in inspect.getmembers(sys.modules[self.module]):
            if inspect.isclass(obj):
               self.classes.append(name)


    def get_result(self):
        loader = unittest.TestLoader()
        suite_list = list()
        for i in range(len(self.classes)):
            mod = getattr(self.mod,self.classes[i])
            suite = unittest.TestSuite((
                loader.loadTestsFromTestCase(mod)
            ))
            suite_list.append(suite)

        runner = unittest.TextTestRunner(verbosity=2)
        list_of_result = list()
        for i in suite_list:
            t = runner.run(i)
            list_of_result.append(1-len(t.failures))
        print("lista wyników unittestów dla wszystkich testów",list_of_result)




g = Get_result_of_tests("tests","test_package")
g.get_result()

