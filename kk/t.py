from kk import foo
import unittest
class C(unittest.TestCase):
	def test(self):
	    self.assertEqual(foo.operator(),11)


main = unittest.main


