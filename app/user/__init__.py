# Import app-based dependencies
from app import app
from util import utils

# Import core libraries
from lib import database
from lib.error_handler import FailedRequest


config = app.config
db = app.db


def add_user(_params):
    database.query(
        db.app_db, 'INSERT INTO users(`user_id`, `email`) VALUES \
        (:user_id, :email)', _params)

    return


def get_user(_params):
    data = database.get(
        db.app_db, 'SELECT * from users WHERE user_id = :user_id', _params)

    if not data:
        raise FailedRequest('User not found')

    return data
