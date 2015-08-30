# Import global context
from flask import redirect, request

# Import app-based dependencies
from util import utils

# Import core libraries
from lib.error_handler import FailedRequest
from lib.response import Response

# Other imports
from functools import wraps
from threading import Thread


def async(f):

    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()

    return wrapper


def make_response(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        response = Response()
        response.set_header('nida', utils.nida())

        return func(res=response, *args, **kwargs)

    return wrapper
