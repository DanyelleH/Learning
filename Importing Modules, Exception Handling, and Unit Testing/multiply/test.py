import unittest
from multiply import multiply_3_numbers

class TestMultiples(unittest.TestCase):

    def test_1(self):
        result = multiply_3_numbers(3,2,4)
        self.assertEqual(result,24)

    def test_1(self):
        result = multiply_3_numbers(2.5,1.5,2.0)
        self.assertEqual(result, 7.5)

if __name__ == "__main__":
    unittest.main()