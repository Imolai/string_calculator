import subprocess
import unittest


class TestStringCalculatorIndependentProgram(unittest.TestCase):
    """Tests for the String Calculator when called as an independent program."""

    def run_program(self, input_string):
        """Run the string calculator program with the given input string."""
        result = subprocess.run(
            ["python3", "string_calculator_program.py", input_string or ""],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )
        return result

    def test_add_two_numbers(self):
        """Test adding two numbers."""
        result = self.run_program("1,2")
        self.assertEqual(result.stdout.strip(), "3")
        result = self.run_program("10,4")
        self.assertEqual(result.stdout.strip(), "14")

    def test_add_empty_string(self):
        """Test handling of an empty string."""
        result = self.run_program("")
        self.assertEqual(result.stdout.strip(), "0")

    def test_add_null(self):
        """Test handling of a null input."""
        result = self.run_program(None)
        self.assertEqual(result.stdout.strip(), "0")

    def test_add_with_default_delimiters(self):
        """Test adding numbers with default delimiters."""
        result = self.run_program("1,2,3")
        self.assertEqual(result.stdout.strip(), "6")

    def test_add_with_different_delimiters(self):
        """Test adding numbers with different delimiters."""
        result = self.run_program("1 2 3")
        self.assertEqual(result.stdout.strip(), "6")

    def test_add_with_custom_delimiters(self):
        """Test adding numbers with custom delimiters."""
        result = self.run_program("//;\n1;2;3")
        self.assertEqual(result.stdout.strip(), "6")

    def test_no_negative_numbers_allowed(self):
        """Test that negative numbers are not allowed."""
        result = self.run_program("1,-2,3")
        self.assertIn("Negative numbers are not allowed", result.stderr)

    def test_ignore_numbers_greater_than_100(self):
        """Test that numbers greater than 100 are ignored."""
        result = self.run_program("1,2,100,101")
        self.assertEqual(result.stdout.strip(), "103")
