# Import app-based dependencies
from app import app

# Import core libraries
from lib import database

db = app.db


def add_user(_params):
    data = database.query(
        db.test_app_db, 'INSERT INTO users(`user_id`, `email`) VALUES(:user_id, :email)', _params)

    return data


def edit_user(_params):
    return _params


def get_user(_params):
    return _params
