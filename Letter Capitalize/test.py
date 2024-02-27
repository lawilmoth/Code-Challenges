import unittest
from problem import letter_capitalize

class TestSolution(unittest.TestCase):
    def test_one_word(self):
        self.assertEqual(letter_capitalize("hello"),"Hello", f'Wrong: got {letter_capitalize("hello")}')
        self.assertEqual(letter_capitalize("yellow"), "Yellow", f'Wrong: got {letter_capitalize("yellow")}')
    def test_upper_case(self):
        self.assertEqual(letter_capitalize("HELLO"),"Hello", f'Wrong: got {letter_capitalize("HELLO")}')
        self.assertEqual(letter_capitalize("GOODLUCK"), "Goodluck", f'Wrong: got {letter_capitalize("GOODLUCK")}')
    def test_with_2_words(self):
        self.assertEqual(letter_capitalize("dont touch"),"Dont Touch", f'Wrong: got {letter_capitalize("dont touch")}')
        self.assertEqual(letter_capitalize("GOOD Job"), "Good Job", f'Wrong: got {letter_capitalize("GOOD Job")}')
if __name__ == "__main__":
    unittest.main()