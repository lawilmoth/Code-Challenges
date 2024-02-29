import unittest
from problem import array_matching

class TestSolution(unittest.TestCase):
    def test_large_num(self):
        self.assertEqual(array_matching("6,5,9"),"6,5,9", f'Wrong: got {array_matching("6,5,9")}')
        self.assertEqual(array_matching("8,3,9"), "8,3,9", f'Wrong: got {array_matching("8,3,9")}')
    def test_upper_case(self):
        self.assertEqual(array_matching("ZYWX"),"wxyz", f'Wrong: got {array_matching("ZYWX")}')
        self.assertEqual(array_matching("GOODLUCK"), "cdgkloou", f'Wrong: got {array_matching("GOODLUCK")}')
    def test_with_symbols(self):
        self.assertEqual(array_matching("ZYWX!?"),"wxyz", f'Wrong: got {array_matching("ZYWX")}')
        self.assertEqual(array_matching("Good luck!"), "cdgkloou", f'Wrong: got {array_matching("GOODLUCK")}')
if __name__ == "__main__":
    unittest.main()