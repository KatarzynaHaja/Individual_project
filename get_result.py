import unittest
import importlib
import sys
import inspect
import imp

class Get_result_of_tests:
    def __init__(self, filename,package):
        self.module = package+'.'+filename
        self.mod = importlib.import_module(self.module)
        importlib.reload(self.mod)
        self.filename = filename
        self.package = package
        self.classes = []
        for name, obj in inspect.getmembers(sys.modules[self.module]):
            if inspect.isclass(obj):
               self.classes.append(name)
        self.clas= "MyTest"
    def get_result(self):
        loader = unittest.TestLoader()
        mod = getattr(self.mod,self.clas)
        suite = unittest.TestSuite((
            loader.loadTestsFromTestCase(mod)
        ))
        print(suite)

       # runner = unittest.TextTestRunner(verbosity=2)
        list_of_result = list()
        for i in suite:
            t = i.run()
            list_of_result.append(1-len(t.failures))
        print("lista wyników unittestów dla wszystkich testów",list_of_result)




# g = Get_result_of_tests("unit","test_package")
# g.get_result()
# #
# g = Get_result_of_tests("tests1","test_package")
# g.get_result()

