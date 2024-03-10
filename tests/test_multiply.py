import unittest
from components import multiply


class TestMultiply(unittest.TestCase):
    def test_multiply_two_positives(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_multiply_two_negatives(self):
        self.assertEqual(multiply(-2, -3), 6)

    def test_multiply_positive_negative(self):
        self.assertEqual(multiply(2, -3), -6)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(5, 0), 0)


if __name__ == "__main__":
    unittest.main()
