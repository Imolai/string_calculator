from http import HTTPStatus as HTTP
from typing import Any, Dict, Union

from flask import jsonify


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
