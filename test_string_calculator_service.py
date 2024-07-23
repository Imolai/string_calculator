import json
import unittest
from http import HTTPStatus as HTTP
from typing import Any, Dict, Optional

from app import app
from flask.testing import FlaskClient


class TestStringCalculatorService(unittest.TestCase):
    """Tests for the String Calculator when called as a service."""

    def setUp(self):
        """Set up the Flask test client."""
        self.app: FlaskClient = app.test_client()
        self.app.testing = True

    def post_numbers(self, numbers: Optional[str]) -> Dict[str, Any]:
        """Helper method to send POST request and parse response."""
        response = self.app.post(
            "/add",
            data=json.dumps({"numbers": numbers}),
            content_type="application/json",
        )
        return json.loads(response.get_data(as_text=True))

    def assert_result(self, numbers: Optional[str], expected_result: int) -> None:
        """Helper method to assert the result from the service."""
        data = self.post_numbers(numbers)
        self.assertEqual(data.get("result"), expected_result)

    def assert_error(self, numbers: Optional[str], expected_error: str) -> None:
        """Helper method to assert the error message from the service."""
        data = self.post_numbers(numbers)
        self.assertEqual(data.get("error"), expected_error)

    def test_main_route(self):
        """Test the main route to ensure it returns the correct HTML form."""
        response = self.app.get("/")
        response_data = response.get_data(as_text=True)
        self.assertEqual(response.status_code, HTTP.OK)
        self.assertIn('<form action="/add" method="POST">', response_data)
        self.assertIn('<input name="numbers">', response_data)
        self.assertIn('<input type="submit" value="Calculate">', response_data)

    def test_add_service_two_numbers(self):
        """Test adding two numbers."""
        self.assert_result("1,2", 3)
        self.assert_result("10,4", 14)

    def test_add_service_empty_string(self):
        """Test handling of an empty string."""
        self.assert_result("", 0)

    def test_add_service_null(self):
        """Test handling of a null input."""
        self.assert_result(None, 0)

    def test_add_service_with_default_delimiters(self):
        """Test adding numbers with default delimiters."""
        self.assert_result("1,2,3", 6)

    def test_add_service_with_different_delimiters(self):
        """Test adding numbers with different delimiters."""
        self.assert_result("1 2 3", 6)

    def test_add_service_with_custom_delimiters(self):
        """Test adding numbers with custom delimiters."""
        self.assert_result("//;\n1;2;3", 6)

    def test_no_negative_numbers_allowed(self):
        """Test that negative numbers are not allowed."""
        self.assert_error("1,-2,3", "Negative numbers are not allowed")

    def test_ignore_numbers_greater_than_100(self):
        """Test that numbers greater than 100 are ignored."""
        self.assert_result("1,2,100,101", 103)

    def test_invalid_json(self):
        """Test that invalid JSON data results in a bad request."""
        response = self.app.post(
            "/add",
            data='["not", "a", "dictionary"]',
            content_type="application/json",
        )
        response_data = response.get_data(as_text=True)

        self.assertEqual(response.status_code, HTTP.BAD_REQUEST)
        self.assertIn("Missing 'numbers' in request", response_data)

    def test_missing_numbers_in_form_data(self):
        """Test that form data without 'numbers' key results in a bad request."""
        response = self.app.post(
            "/add",
            data={"key": "value"},
            content_type="application/x-www-form-urlencoded",
        )
        response_data = response.get_data(as_text=True)

        self.assertEqual(response.status_code, HTTP.BAD_REQUEST)
        self.assertIn("Missing 'numbers' in request", response_data)
