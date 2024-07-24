import unittest

from string_calculator import StringCalculator


class TestStringCalculator(unittest.TestCase):
    """Tests for the String Calculator when used as a library function."""

    def setUp(self):
        """Set up the StringCalculator instance."""
        self.calc = StringCalculator()

    def test_add_two_numbers(self):
        """Test adding two numbers."""
        self.assertEqual(self.calc.add("1,2"), 3)
        self.assertEqual(self.calc.add("10,4"), 14)

    def test_add_empty_string(self):
        """Test handling of an empty string."""
        self.assertEqual(self.calc.add(""), 0)

    def test_add_null(self):
        """Test handling of a null input."""
        self.assertEqual(self.calc.add(None), 0)

    def test_add_with_default_delimiters(self):
        """Test adding numbers with default delimiters."""
        self.assertEqual(self.calc.add("1,2,3"), 6)

    def test_add_with_different_delimiters(self):
        """Test adding numbers with different delimiters."""
        self.assertEqual(self.calc.add("1 2 3"), 6)

    def test_add_with_custom_delimiters(self):
        """Test adding numbers with custom delimiters."""
        self.assertEqual(self.calc.add("//;\n1;2;3"), 6)

    def test_integer_numbers_allowed(self):
        """Test that non integer numbers are not allowed."""
        with self.assertRaises(ValueError):
            self.calc.add("1,2,3.14")

    def test_no_negative_numbers_allowed(self):
        """Test that negative numbers are not allowed."""
        with self.assertRaises(ValueError):
            self.calc.add("1,-2,3")

    def test_ignore_numbers_greater_than_100(self):
        """Test that numbers greater than 100 are ignored."""
        self.assertEqual(self.calc.add("1,2,100,101"), 103)
