import unittest
from Day1_Exercise1 import process_numbers

class TestNumberProcessing(unittest.TestCase):
    test_numbers = [2, 3, 6, 0, -1, -4]
    def test_sum_even(self):
        self.assertDictEqual(process_numbers(self.test_numbers), {'product_odd': -3, 'sum_even': 4, 'count_positives': 3, 'count_negatives': 2, 'count_zeros': 1}, "Test of process_numbers failed :(")

if __name__ == "__main__":
    unittest.main()