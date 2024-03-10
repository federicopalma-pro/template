import unittest
from components import divide


class TestDivide(unittest.TestCase):
    def test_divide_two_positives(self):
        self.assertEqual(divide(6, 3), 2)

    def test_divide_two_negatives(self):
        self.assertEqual(divide(-6, -3), 2)

    def test_divide_positive_negative(self):
        self.assertEqual(divide(6, -3), -2)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(5, 0)


if __name__ == "__main__":
    unittest.main()
