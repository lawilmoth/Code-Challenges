import unittest
from problem import BinaryConverter

class TestSolution(unittest.TestCase):
    def test_Binarconverter(self):
        self.assertEqual(BinaryConverter("100101"),"37", f'Wrong: got {BinaryConverter("100101")}')
        self.assertEqual(BinaryConverter("101101"), "45", f'Wrong: got {BinaryConverter("101101")}')
    
if __name__ == "__main__":
    unittest.main()
