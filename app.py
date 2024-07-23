from http import HTTPStatus as HTTP
from typing import Any, Dict, Union

from flask import Flask, jsonify, request
from string_calculator import StringCalculator

app = Flask(__name__)
calc = StringCalculator()


def json_response(message: Union[str, Dict[str, Any]], status: HTTP) -> tuple:
    """
    Helper function to create a standardized JSON response.

    Args:
        message (Union[str, Dict[str, Any]]): The message or data to include in the response.
        status (HTTP): The HTTP status code.

    Returns:
        tuple: A tuple containing the JSON response and the status code.
    """
    if isinstance(message, str):
        return jsonify({"error": message}), status
    return jsonify(message), status


@app.route("/")
def main() -> str:
    """
    Main route to display a form for user input and handle form submission.

    Returns:
        str: HTML content for the form and result.
    """
    return """
    <form action="/add" method="POST">
        <input name="numbers">
        <input type="submit" value="Calculate">
    </form>
    """


@app.route("/add", methods=["POST"])
def add() -> Union[Dict[str, Any], tuple]:
    """
    Endpoint to add numbers from a JSON or form request.

    Returns:
        Union[Dict[str, Any], tuple]: JSON response containing the result or an error message.
    """
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form.to_dict()

    if not isinstance(data, dict) or "numbers" not in data:
        return json_response("Missing 'numbers' in request", HTTP.BAD_REQUEST)

    numbers = data.get("numbers", "")
    try:
        result = calc.add(numbers)
        return json_response({"result": result}, HTTP.OK)
    except ValueError as e:
        return json_response(str(e), HTTP.BAD_REQUEST)
