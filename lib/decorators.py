# Import global context
from flask import redirect, request

# Import app-based dependencies
from util import utils

# Import core libraries
from lib.error_handler import FailedRequest
from lib.response import Response

# Other imports
from functools import wraps


def make_response(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        response = Response()

        return func(res=response, *args, **kwargs)

    return wrapper
