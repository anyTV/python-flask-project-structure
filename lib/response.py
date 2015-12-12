# Import global context
from flask import jsonify, make_response, redirect, Response as resp

# Import app-based dependencies
from util import utils


class Response:

    def __init__(self):
        self.headers = {}

    def set_header(self, key, value):
        self.headers[key] = value

    def send(self, data):
        response = make_response(jsonify({'data': data}))

        # set this later in config
        response.mimetype = 'application/json'

        response.status = '200'

        for key in self.headers:
            response.headers.add(key, self.headers[key])

        return response

    def stream(self, data, mimetype='application/octet-stream'):
        response = resp(data)

        response.mimetype = mimetype
        response.status = '200'

        for key in self.headers:
            response.headers.add(key, self.headers[key])

        return response

    def redirect(self, url, params):
        response = make_response(
            redirect(url + '?' + utils.encode_params(params)))

        return response
