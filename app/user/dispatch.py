# Import global context
from flask import request

# Import flask dependencies
from flask import Blueprint

# Import app-based dependencies
from app import user

# Import core libraries
from lib.decorators import sample_decorator


# Define the blueprint: 'user', set its url prefix: app.url/user
mod_user = Blueprint('user', __name__)


# Declare all the routes

@mod_user.route('/', methods=['GET'])
@sample_decorator
def get_user(data):

    print data
    params = {
        'user_id' : request.user_id
    }

    return res.send(user.get_user(params)[0])


@mod_user.route('/', methods=['POST'])
def edit_user(res):
    params = {
        'user_id'   : request.user_id,
        'active'    : request.form['active'],
        'rank'      : request.form['rank']
    }

    user.edit_user(params)

    return res.send('edit success')


@mod_user.route('/scope', methods=['GET'])
def get_scopes(res):
    params = {
        'user_id' : request.user_id
    }

    return res.send(user.get_scopes(params))

