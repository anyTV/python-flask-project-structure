
# Mongo db config
MONGO_URI = '127.0.0.1'
MONGO_HOST = 'localhost'
MONGO_PORT = '27017'
MONGO_CONNECT_TIMEOUT_MS = 10000


# MySQL Config
# For multiple mysql connections, use object for each config,
# the db driver will read and parse it as needed

DB = {
    'host': 'localhost',
    'db': 'app',
    'user': 'root',
    'password': '',
    'port': 3306
}
