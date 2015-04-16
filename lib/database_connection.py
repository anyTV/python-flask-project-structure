# Import flask dependencies
from flask import Blueprint

# Import development environment
from instance.env import development

# Import core libraries
from lib import database


class Database():

    def __init__(self):
        self.engines = []

    def add_engine(self, config):
        engine = database.make_engine_with_session(config)
        self.engines.append(engine)
        return engine


# Blueprint declaration
mod_db_connection = Blueprint('mod_db_connection', __name__)

db = Database()

# Database connections declaration
# If you want global accessisble database, declare it here
# It will automatically give you a connection from the connection pool
db.test_app_db = db.add_engine(development.MYSQL_CONNECTION)


@mod_db_connection.teardown_app_request
def shutdown_session(exception=None):
    """Remove the local session after executing the request."""
    for engine in db.engines:
        engine.remove()


def get_database():
    return db
