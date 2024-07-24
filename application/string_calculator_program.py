import argparse
import logging
import sys

from library.string_calculator import StringCalculator

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def main() -> None:
    """Main function to run the String Calculator as an independent program."""
    parser = argparse.ArgumentParser(description="Run the String Calculator.")
    parser.add_argument(
        "numbers",
        help="A string containing numbers separated by delimiters.",
    )
    args = parser.parse_args()

    numbers = args.numbers
    calc = StringCalculator()

    try:
        result = calc.add(numbers)
        print(result)
    except ValueError as exc:
        logging.error("Error: %s", exc)
        sys.exit(1)


if __name__ == "__main__":
    main()
