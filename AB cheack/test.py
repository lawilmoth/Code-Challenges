import unittest
from problem import ab_check

class TestSolution(unittest.TestCase):
    def test_(self):
        self.assertEqual(ab_check("a   b"),"agggb" ,f'expected "agggb", but got {ab_check("abba")}')
    def test_(self):
        self.assertEqual(ab_check("agggb"),"ahggb" ,f'expected "ahggb", but got {ab_check("ahgggb")}')    
    def test_(self):
        self.assertEqual(ab_check("afhgbhgayghb"),"ajggblmnamnhb" ,f'expected "ajggblmnamnh", but got {ab_check("abghtab")}')
  

if __name__ == "__main__":
    unittest.main()