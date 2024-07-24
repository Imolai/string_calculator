# String Calculator

## Table of Contents

- [String Calculator](#string-calculator)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage](#usage)
    - [As a Library](#as-a-library)
    - [As an Independent Program](#as-an-independent-program)
    - [As a Service](#as-a-service)
  - [Running Tests](#running-tests)
    - [Test as a Library](#test-as-a-library)
    - [Test as an Independent Program](#test-as-an-independent-program)
    - [Test as a Service](#test-as-a-service)
  - [Extensibility](#extensibility)
  - [FAQ](#faq)
    - [How can I use the string calculator?](#how-can-i-use-the-string-calculator)
    - [Is it extendable with new functionalities and constraints?](#is-it-extendable-with-new-functionalities-and-constraints)
    - [What delimiters do I accept and why?](#what-delimiters-do-i-accept-and-why)
    - [How do I handle exceptions?](#how-do-i-handle-exceptions)
    - [What are constraints on input and output?](#what-are-constraints-on-input-and-output)
    - [How should tests be organized?](#how-should-tests-be-organized)
  - [Docker Usage](#docker-usage)
    - [Building the Docker Image](#building-the-docker-image)
    - [Running the Docker Container](#running-the-docker-container)
    - [Accessing the Application](#accessing-the-application)
  - [Pre-commit Hooks](#pre-commit-hooks)

## Description

This is a simple string calculator implemented with a Test Driven (TDD) approach in Python. The calculator adds numbers present in a string, with support for different delimiters, handling empty
or null input, and ignoring numbers greater than 100. Negative numbers are not allowed.

## Requirements

- Python v3.x
- Flask (for the service)

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/Imolai/string_calculator.git
   ```

2. Navigate to the project directory:

   ```sh
   cd string_calculator
   export PYTHONPATH=$(pwd)
   ```

3. Create and activate a virtual environment:

   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On macOS/Linux
   # or
   .\.venv\Scripts\activate  # On Windows
   ```

4. Install the required packages:

   ```sh
   pip install -r service/requirements.txt
   ```

## Usage

### As a Library

To use the string calculator as a library, create an instance of the `StringCalculator` class and
call the `add` method:

```python
from library.string_calculator import StringCalculator

calc = StringCalculator()
result = calc.add("1,2,3")
print(result)  # Output: 6
```

### As an Independent Program

To use the string calculator as an independent program:

1. Run the script with an argument:

   ```sh
   python application/string_calculator_program.py "1,2,3" # Output: 6
   ```

### As a Service

To use the string calculator as a web service:

1. Run the Flask application:

   ```sh
   FLASK_APP=service/app.py FLASK_DEBUG=1 FLASK_ENV=development flask run
   ```

2. Send a POST request to the service:

   ```sh
   curl -X POST http://127.0.0.1:5000/add -H "Content-Type: application/json" -d '{"numbers": "1,2,3"}'
   ```

   Output:

   ```json
   {
      "result": 6
   }
   ```

> The console message "WARNING: This is a development server. Do not use it in a production
> deployment. Use a production WSGI server instead." is normal. Follow the advice and install the
> service into a [Gunicorn WSGI server](https://gunicorn.org/). Press CTRL+C to quit the service.

## Running Tests

### Test as a Library

To run the tests for the library, use the following command:

```sh
python -m unittest tests/test_string_calculator.py
```

### Test as an Independent Program

To run the tests for the independent program, use the following command:

```sh
python -m unittest tests/test_string_calculator_program.py
```

### Test as a Service

To run the tests for the service, use the following command:

```sh
python -m unittest tests/test_string_calculator_service.py
```

## Extensibility

- The `StringCalculator` class can be extended with new functionalities and constraints.
- Additional delimiters can be added to the `__default_delimiters` list.
- Custom exception handling can be implemented as needed.

## FAQ

### How can I use the string calculator?

This can be used as an independent program, a library function, or a service.

### Is it extendable with new functionalities and constraints?

Yes, the code is designed to be extendable:

- We can easily extend the `StringCalculator` class to support new delimiters by modifying the `__default_delimiters` list field or adding a new method to set custom delimiters.
- We can add operations as new methods and new endpoints of the Flask app to support additional
  operations (e.g., subtracting, multiplying numbers, etc.).
- We can extend the `StringCalculator` class to ignore specific numbers, so we can add an additional
  list field to the class (e.g. `__ignored_numbers`) to specify the numbers to be ignored.

### What delimiters do I accept and why?

The default delimiters are comma (`,`) and space (` `), see in the `__default_delimiters` list
field. Custom delimiters can be specified at the beginning of the input string.

### How do I handle exceptions?

Currently, the code raises a `ValueError` for negative numbers. Additional exception handling can be
added as required. For example, the code ignores numbers greater than 100 silently according to the
requirements. But we can change this behavior by raising a `ValueError` exception too. Or, we can
define a custom exception for the `StringCalculator` by inheriting the `Exception` class.

### What are constraints on input and output?

Input should be a string containing positive integer numbers and delimiters and maybe spaces. Custom
delimiters are also allowed. Output is an integer sum of the numbers. In case of any error, an error
message ("invalid literal for int() with base 10: '...'"). Or, `ValueError` exception for
non-integer or negative numbers.

### How should tests be organized?

Tests are organized using the `unittest` framework in separate test files for different usages:

- A library function (tests of all of the library functionality).
- An independent program (tests of the CLI).
- A service (tests of the Web UI).

## Docker Usage

### Building the Docker Image

```sh
docker build -t string-calculator -f service/Dockerfile .
```

### Running the Docker Container

```sh
docker run -d -p 5000:5000 string-calculator
```

### Accessing the Application

Open your browser and go to `http://localhost:5000`.

## Pre-commit Hooks

Pre-commit hooks are installed and configured in this project to ensure code quality and consistency
before each commit. They automatically run checks like `mypy` for type checking, preventing code
that doesn't meet the defined standards from being committed. This helps maintain code integrity and
reduces errors. The necessary configuration is already included in the repository.
