# Import global context
from flask import request

# Import flask dependencies
from flask import Blueprint

# Import app-based dependencies
from app import user
from util import utils

# Import core libraries
from lib.decorators import make_response

# Define the blueprint: 'user', set its url prefix: app.url/user
mod_user = Blueprint('user', __name__)


# Declare all the routes

@mod_user.route('/<user_id>', methods=['GET'])
@make_response
def get_user(res, user_id):

    result = user.get_user(user_id)
    return res.send(result)


@mod_user.route('/', methods=['POST'])
def add_user(res):

    params = utils.get_data(['user_id', 'email'], request.values)

    user.add_user(params)

    return res.send('Successfully added user')
