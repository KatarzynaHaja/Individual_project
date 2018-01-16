import unittest 
from codes.neww import *
class MyTest(unittest.TestCase): 
    def test0(self):
        self.assertEqual(func1(1,5),-1)
    def test1(self):
        self.assertEqual(func2(3,8),0)
    def test2(self):
        self.assertEqual(func12(6,2),-1)
    def test3(self):
        self.assertEqual(func24(8,10),0)
    def test4(self):
        self.assertEqual(func34(8,10),747478801)
    def test5(self):
        self.assertEqual(func46(1,9),935499983)
    def test6(self):
        self.assertEqual(func49(7,10),0)
