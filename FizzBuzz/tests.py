import unittest
from problem import fizz_buzz

class TestSolution(unittest.TestCase):
    def test_one(self):
        self.assertEqual(fizz_buzz(8),
        "1 2 Fizz 4 Buzz Fizz 7 8",
        f'Expected "1 2 Fizz 4 Buzz Fizz 7 8", but got {fizz_buzz(8)}')
    def test_two(self):
        self.assertEqual(fizz_buzz(18),
        "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz",
        f'Expected "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz", but got {fizz_buzz(18)}')
    def test_three(self):
        self.assertEqual(fizz_buzz(12),
        "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz",
        f'Expected "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz", but got {fizz_buzz(12)}')




if __name__ == "__main__":
    unittest.main()
