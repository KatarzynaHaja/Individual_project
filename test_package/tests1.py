import unittest

import M0test

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(M0test.operator(), 124)

    def test1(self):
        self.assertEqual(M0test.operator(), 111)



if __name__ == '__main__':
    unittest.main()