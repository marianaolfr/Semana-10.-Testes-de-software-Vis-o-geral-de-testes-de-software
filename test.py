import unittest
from romanos.conversor import converte

class TestRomanNumeralConverter(unittest.TestCase):
    def test_basic_cases(self):
        self.assertEqual(converte("I"), 1, "Failed to convert 'I' to 1")

    def test_large_numbers(self):
        self.assertEqual(converte("MMMCMXCIX"), 3999, "Failed to convert large number")

    def test_complex_combinations(self):
        self.assertEqual(converte("MCMXCIX"), 1999, "Failed to convert complex combination")

    def test_invalid_inputs(self):
        with self.assertRaises(KeyError):
            converte("Z")  # Invalid character
        with self.assertRaises(ValueError):
            converte("IIII")  # Invalid repetition of I
