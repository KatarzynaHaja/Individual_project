import importlib
import re
import os
import unittest
import inspect
import sys

class Run:
    def __init__(self, filename, package):
        self.module = package + '.' + re.sub(".py", "", filename)
        self.mod = importlib.import_module(self.module)
        self.filename = filename
        self.package = package
        self.path = os.path.join(package, filename)
        self.classes = list()
        self.result = list()
        for name, obj in inspect.getmembers(sys.modules[self.module]):
            if inspect.isclass(obj):
                self.classes.append(name)
        self.clas = self.classes[0]

    def run(self):
        loader = unittest.TestLoader()
        suite_list = list()

        mod = getattr(self.mod, self.clas)
        suite = unittest.TestSuite((
            loader.loadTestsFromTestCase(mod)
        ))
        suite_list.append(suite)

        runner = unittest.TextTestRunner(verbosity=2)
        for i in suite:
            t = runner.run(i)

r = Run("unit.py","test_package")
r.run()