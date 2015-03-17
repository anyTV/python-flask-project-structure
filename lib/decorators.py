# Import global context
from flask import redirect, request

# Import app-based dependencies
from util import utils

# Import core libraries
from lib.response import Response

# Other imports
from functools import wraps


def sample_decorator(func):
    
    @wraps(func)
    def wrapper(*args, **kw):
        data = 'do additional processing before going to routes'

        return func(data = data, *args, **kw)

    return wrapper

