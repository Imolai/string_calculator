import argparse
import sys

from string_calculator import StringCalculator


def main() -> None:
    """Main function to run the String Calculator as an independent program."""
    parser = argparse.ArgumentParser(description="Run the String Calculator.")
    parser.add_argument(
        "numbers", help="A string containing numbers separated by delimiters."
    )
    args = parser.parse_args()

    numbers = args.numbers
    calc = StringCalculator()

    try:
        result = calc.add(numbers)
        print(result)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
