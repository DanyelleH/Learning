import unittest
from functions import list_max

class TestListMax(unittest.TestCase):
    
    def test_1(self):
        # Test a list of all positive values
        a_list =[6,43,18,100,9,85]
        result = list_max(a_list)
        self.assertEqual(result, 100)

    def test_2(self):
        # test list of negative values
        a_list= [-1,-4,-10,-22]
        result = list_max(a_list)
        self.assertEqual(result, -1)

if __name__ == "__main__":
    unittest.main()