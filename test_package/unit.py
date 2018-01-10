import unittest 
from codes.neww import *
class MyTest(unittest.TestCase): 
    def test1(self):
        self.assertEqual(func1(1,5),-2086180971)
    def test2(self):
        self.assertEqual(func2(3,8),-55)
    def test3(self):
        self.assertEqual(func8(6,2),128276356570)
    def test4(self):
        self.assertEqual(func23(8,10),813547601)
    def test5(self):
        self.assertEqual(func29(8,10),-349600642)
    def test6(self):
        self.assertEqual(func30(1,9),-1871180500)
    def test7(self):
        self.assertEqual(func42(7,10),10)
