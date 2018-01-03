import unittest
from mut import *
from os import listdir
from os.path import isfile, join
import re
onlyfiles = [f for f in listdir("../mut") if isfile(join("../mut", f))]
print(onlyfiles)
#tutaj chyba trzeba przepisać unittest dla wszystkch plików z mutacji
class MyTest(unittest.TestCase):
    def test(self):
        for i in onlyfiles:
            i = "../mut/"+i
            self.assertEqual(exec(compile(open(i),"rb").read(), i, 'exec').operator(), 124)