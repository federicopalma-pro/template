import unittest
from components.function import text_up

class TestTextUp(unittest.TestCase):

    def test_text_up_with_lowercase(self):
        result = text_up("hello")
        self.assertEqual(result, "HELLO")

    def test_text_up_with_mixed_case(self):
        result = text_up("HeLLo WoRLd")
        self.assertEqual(result, "HELLO WORLD")

    def test_text_up_with_uppercase(self):
        result = text_up("ALREADY UPPERCASE")
        self.assertEqual(result, "ALREADY UPPERCASE")

    def test_text_up_with_empty_string(self):
        result = text_up("")
        self.assertEqual(result, "")

    def test_text_up_with_numbers_and_symbols(self):
        result = text_up("Hello123!@#")
        self.assertEqual(result, "HELLO123!@#")

if __name__ == '__main__':
    unittest.main()
