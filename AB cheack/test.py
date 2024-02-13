import unittest
from problem import ab_check

class TestSolution(unittest.TestCase):
    def test1_(self):
        self.assertEqual(ab_check("a   b"),True ,f'expected "agggb", but got {ab_check("a   b")}')
    def test2_(self):
        self.assertEqual(ab_check("agggb"),True ,f'expected "ahggb", but got {ab_check("agggb")}')    
    def test3_(self):
        self.assertEqual(ab_check("afhgbhgayghb"),False ,f'expected "ajggblmnamnh", but got {ab_check("abghtab")}')
  

if __name__ == "__main__":
    unittest.main()