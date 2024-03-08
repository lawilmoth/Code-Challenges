import unittest
from problem import basic_roman_numerals

class TestSolution(unittest.TestCase):
    def test_roman_numeral(self):
        self.assertEqual(basic_roman_numerals("I"),1, 
        f'Wrong: got {basic_roman_numerals("I")}')
        
        self.assertEqual(basic_roman_numerals("II"), 2,
        f'Wrong: got {basic_roman_numerals("II")}')
        
    def test_lower_case(self):
        self.assertEqual(basic_roman_numerals("i"), 1, 
        f'Wrong: got {basic_roman_numerals("i")}')
        
        self.assertEqual(basic_roman_numerals("iv"), 4, 
        f'Wrong: got {basic_roman_numerals("iv")}')
        
    def test_with_symbols(self):
        self.assertEqual(basic_roman_numerals("I!?"), 4, 
        f'Wrong: got {basic_roman_numerals("I!?")}')
        
        self.assertEqual(basic_roman_numerals("II!"), 2, 
        f'Wrong: got {basic_roman_numerals("II!")}')
 
        
if __name__ == "__main__":
    unittest.main()