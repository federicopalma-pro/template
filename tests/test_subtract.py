import unittest
from components import subtract


class TestSubtract(unittest.TestCase):
    def test_subtract_two_positives(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_subtract_two_negatives(self):
        self.assertEqual(subtract(-5, -3), -2)

    def test_subtract_positive_negative(self):
        self.assertEqual(subtract(5, -3), 8)

    def test_subtract_zeroes(self):
        self.assertEqual(subtract(0, 0), 0)


if __name__ == "__main__":
    unittest.main()
