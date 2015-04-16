# Import global context
from flask import jsonify, make_response

# Import flask dependencies
from flask import Blueprint


class FailedRequest(Exception):
    status_code = 404

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = {}
        rv['message'] = self.message
        rv['data'] = dict(self.payload or ())
        return rv


# Blueprint declaration
mod_err = Blueprint('mod_err', __name__)


# Declare necessary error handlers

@mod_err.app_errorhandler(404)
def not_found(error):
    return make_response(jsonify({'HTTP 500': 'The Monkey Ninja cannot find your request'}), 404)


@mod_err.app_errorhandler(500)
def not_found(error):
    return make_response(jsonify({'HTTP 500': 'The Monkey Ninja failed internally'}), 500)


@mod_err.app_errorhandler(FailedRequest)
def exception_encountered(error):
    return make_response(jsonify(error.to_dict()), error.status_code)


@mod_err.app_errorhandler(Exception)
def exception_encountered(error):
    return make_response(jsonify({'error': error.message}), 500)
