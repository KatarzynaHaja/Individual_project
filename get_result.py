import unittest
from test_package import tests  #problem z tym importem !!!!!!
from inspect import isclass
import sys
import importlib.util
import imp
import os
import test_package


class Get_result_of_tests:
    def __init__(self, filename,package):

        self.filename = filename
        self.package = package
        self.classes = [x for x in dir(self.filename) if isclass(getattr(self.filename, x))]
        print(self.classes)


    def get_result(self):
        loader = unittest.TestLoader()
        suite_list = list()
        for i in range(len(self.classes)):
            suite = unittest.TestSuite((
                loader.loadTestsFromTestCase(self.filename +'.'+self.classes[i])
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

