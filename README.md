# String Calculator

## Description

This is a simple string calculator implemented with a Test Driven (TDD) approach in Python.
The calculator adds numbers present in a string, with support for different delimiters, handling
empty or null input, and ignoring numbers greater than 100. Negative numbers are not allowed.

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
   ```

3. Install the required packages:

   ```sh
   pip install Flask
   ```

## Usage

### As a Library

To use the string calculator as a library, create an instance of the `StringCalculator` class and
call the `add` method:

```python
from string_calculator import StringCalculator

calc = StringCalculator()
result = calc.add("1,2,3")
print(result)  # Output: 6
```

### As an Independent Program

To use the string calculator as an independent program:

1. Run the script with an argument:

   ```sh
   python string_calculator_program.py "1,2,3" # Output: 6
   ```

### As a Service

To use the string calculator as a web service:

1. Run the Flask application:

   ```sh
   FLASK_APP=app FLASK_DEBUG=1 FLASK_ENV=development flask run
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
> deployment. Use a production WSGI server instead." is normal, it will be removed if you follow the
> advice and install the service into e.g. a [Gunicorn WSGI server](https://gunicorn.org/). Press
> CTRL+C to quit the service.

## Running Tests

### Test as a Library

To run the tests for the library, use the following command:

```sh
python -m unittest test_string_calculator.py
```

### Test as an Independent Program

To run the tests for the independent program, use the following command:

```sh
python -m unittest test_string_calculator_program.py
```

### Test as a Service

To run the tests for the service, use the following command:

```sh
python -m unittest test_string_calculator_service.py
```

## Extensibility

- The `StringCalculator` class can be extended with new functionalities and constraints.
- Additional delimiters can be added to the `default_delimiters` list.
- Custom exception handling can be implemented as needed.

## FAQ

### How can I use the string calculator?

This can be used as an independent program, a library function, or a service.

### Is it extendable with new functionalities and constraints?

Yes, the code is designed to be extendable.

### What delimiters do I accept and why?

The default delimiters are comma (`,`) and space (` `).

Custom delimiters can be specified at the beginning of the input string.

### How do I handle exceptions?

Currently, the code raises a `ValueError` for negative numbers. Additional exception handling can be
added as required.

### What are constraints on input and output?

Input should be a string. Output is an integer sum of the numbers.

### How should tests be organized?

Tests are organized using the `unittest` framework in separate test files for different usages.

## Table of Contents

- [String Calculator](#string-calculator)
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
  - [Table of Contents](#table-of-contents)
