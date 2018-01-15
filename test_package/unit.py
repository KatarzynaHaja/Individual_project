import unittest 
from codes.neww import *

class MyTest(unittest.TestCase): 
    def test1(self):
        self.assertEqual(func1(1,5),0)
    def test2(self):
        self.assertEqual(func11(3,8),3163826106)
    def test3(self):
        self.assertEqual(func12(6,2),2113928959)
    def test4(self):
        self.assertEqual(func13(8,10),1832)
    def test5(self):
        self.assertEqual(func14(8,10),10)
    def test6(self):
        self.assertEqual(func20(1,9),91079796)
    def test7(self):
        self.assertEqual(func31(7,10),-1170)
    def test8(self):
        self.assertEqual(func44(6,10),1356108288)
    def test9(self):
        self.assertEqual(func45(9,7),68191224)
    def test10(self):
        self.assertEqual(func55(7,3),-2096559865)
