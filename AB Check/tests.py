import unittest
from problem import ab_check

class TestSolution(unittest.TestCase):
    def test_a_b_false(self):
        self.assertEqual(ab_check('after badly'), 
                        False,
                        f'Expected "False", but got {ab_check("after badly")}'
                        )
        
    def test_a_b_true(self):
        self.assertEqual(ab_check('Laura sobs'), 
                        True,
                        f'Expected "True", but got {ab_check("Laura sobs")}'
                        )
        
        self.assertEqual(ab_check('Aura'),
                        True,
                        f'Expected "True", but got {ab_check("Aura")}')

if __name__ == "__main__":
    unittest.main()