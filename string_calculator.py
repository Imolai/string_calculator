import re
from typing import List, Optional


class StringCalculator:
    """A simple string calculator to add numbers from a string input."""

    def __init__(self):
        """Initialize the StringCalculator with default delimiters."""
        self.__default_delimiters = [",", " "]

    @property
    def default_delimiters(self) -> List[str]:
        """
        Get the default delimiters.

        Returns:
            List[str]: The list of default delimiters.
        """
        return self.__default_delimiters.copy()

    def add(self, numbers: Optional[str]) -> int:
        """
        Add numbers present in the input string.

        Args:
            numbers (str): A string containing numbers separated by delimiters.
                To add custom delimiter, e.g. ";", `numbers` is "//;\\n1;2;3"

        Returns:
            int: The sum of the numbers in the input string.

        Raises:
            ValueError: If a negative number is found in the input.
        """
        if not numbers:
            return 0

        # Handle custom delimiters
        delimiters = self.default_delimiters
        if numbers.startswith("//"):
            parts = numbers.split("\n", 1)
            delimiters.append(parts[0][2:])
            numbers = parts[1]

        # Split by delimiters
        regex_pattern = "|".join([re.escape(delimiter) for delimiter in delimiters])
        num_list = re.split(regex_pattern, numbers)

        # Sum the numbers
        total = 0
        for num in num_list:
            if num:
                try:
                    value = int(num)
                except ValueError as value_exception:
                    raise ValueError(
                        "Non integer numbers are not allowed"
                    ) from value_exception
                if value < 0:
                    raise ValueError("Negative numbers are not allowed")
                if value <= 100:
                    total += value

        return total
