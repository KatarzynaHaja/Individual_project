import unittest 
from codes.neww import *

class MyTest(unittest.TestCase): 
    def test1(self):
        self.assertEqual(func1(1,5),281472432173822)
    def test2(self):
        self.assertEqual(func11(3,8),641)
    def test3(self):
        self.assertEqual(func12(6,2),-1483746702)
    def test4(self):
        self.assertEqual(func13(8,10),-1172329106)
    def test5(self):
        self.assertEqual(func15(8,10),-501)
    def test6(self):
        self.assertEqual(func16(1,9),-1294075175)
    def test7(self):
        self.assertEqual(func21(7,10),-1420329748)
    def test8(self):
        self.assertEqual(func29(6,10),-1420035649)
    def test9(self):
        self.assertEqual(func30(9,7),1562983194)
    def test10(self):
        self.assertEqual(func31(7,3),-1879334913)
    def test11(self):
        self.assertEqual(func32(1,2),304376079)
    def test12(self):
        self.assertEqual(func44(2,7),1718582416)
    def test13(self):
        self.assertEqual(func45(3,2),-23)
    def test14(self):
        self.assertEqual(func51(3,9),3497367597)
