# Import global context
from flask import current_app as app

# Import app-based dependencies
from util import utils

# Import core libraries
from lib.response import Response

# Other imports
from functools import wraps
from threading import Thread


def async(f):
    def wrapper(*args, **kwds):
        return app.pool.apply_async(f, args=args, kwds=kwds)

    return wrapper


def async_threaded(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()

    return wrapper


def make_response(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        response = Response()

        return func(res=response, *args, **kwargs)

    return wrapper
