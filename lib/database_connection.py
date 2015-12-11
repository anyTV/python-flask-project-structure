# Import flask dependencies
from flask import Blueprint

# Import core libraries
from lib import database


class Database:

    def __init__(self):
        self.engines = []

    def add_engine(self, config):
        engine = database.make_engine(config)
        self.engines.append(engine)
        return engine


# Blueprint declaration
mod_db_connection = Blueprint('mod_db_connection', __name__)

db = Database()


def add_databases(_config):
    db.app_db = db.add_engine(_config['DB'])
