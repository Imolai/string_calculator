import subprocess
import unittest


class TestStringCalculatorIndependentProgram(unittest.TestCase):
    """Tests for the String Calculator when called as an independent program."""

    def run_program(self, *args):
        """Run the string calculator program with the given input string."""
        result = subprocess.run(
            ["coverage", "run", "string_calculator_program.py", *args],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False,
        )
        return result

    def test_no_arguments(self):
        """Test running the program without arguments."""
        result = self.run_program()
        self.assertIn("usage: string_calculator_program.py [-h] numbers", result.stderr)
        self.assertIn(
            "error: the following arguments are required: numbers", result.stderr
        )

    def test_help_option(self):
        """Test running the program with -h option."""
        result = self.run_program("-h")
        self.assertIn("usage: string_calculator_program.py [-h] numbers", result.stdout)
        self.assertIn("Run the String Calculator.", result.stdout)
        self.assertIn("positional arguments:", result.stdout)
        self.assertIn(
            "numbers     A string containing numbers separated by delimiters.",
            result.stdout,
        )
        self.assertIn("options:", result.stdout)
        self.assertIn("-h, --help  show this help message and exit", result.stdout)

    def test_help_option_long(self):
        """Test running the program with --help option."""
        result = self.run_program("--help")
        self.assertIn("usage: string_calculator_program.py [-h] numbers", result.stdout)
        self.assertIn("Run the String Calculator.", result.stdout)
        self.assertIn("positional arguments:", result.stdout)
        self.assertIn(
            "numbers     A string containing numbers separated by delimiters.",
            result.stdout,
        )
        self.assertIn("options:", result.stdout)
        self.assertIn("-h, --help  show this help message and exit", result.stdout)

    def test_valid_input(self):
        """Test running the program with valid input."""
        result = self.run_program("1,2,3")
        self.assertEqual(result.stdout.strip(), "6")

    def test_extra_arguments(self):
        """Test running the program with extra arguments."""
        result = self.run_program("1,2,3", "arg2")
        self.assertIn("usage: string_calculator_program.py [-h] numbers", result.stderr)
        self.assertIn("error: unrecognized arguments: arg2", result.stderr)

    def test_negative_number(self):
        """Test running the program with negative numbers which should raise ValueError."""
        result = self.run_program("1,-2,3")
        self.assertIn("Error: Negative numbers are not allowed", result.stderr)
        self.assertNotEqual(result.returncode, 0)
