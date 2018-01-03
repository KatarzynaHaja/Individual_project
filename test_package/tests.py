import unittest

from kk import foo


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(foo.operator(), 124)

    def test1(self):
        self.assertEqual(foo.operator(), 111)




if __name__ == '__main__':
    unittest.main()