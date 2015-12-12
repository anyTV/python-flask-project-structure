# Import global context
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.sql import text


def sql_alchemy_format(_config):
    return 'mysql+pymysql://' + _config['user'] + ':' + _config['password'] + '@' + \
        _config['host'] + ':' + str(_config['port']) + '/' + _config['db']


# Creates an engine
def make_engine(_config):
    return create_engine(sql_alchemy_format(_config), pool_recycle=3600,
                         pool_size=20, pool_timeout=60)


# Executes db get
def get(_db, _query, _params={}):
    result = []

    try:
        data = _db.execute(text(_query), _params)

    except OperationalError:
        return get(_db, _query, _params)

    for row in data:
        result.append(dict(row) or row)

    return result


# Executes raw query
def query(_db, _query, _params={}):
    result = {}

    try:
        data = _db.execute(text(_query), _params)

    except OperationalError:
        return query(_db, _query, _params)

    if data.rowcount == 0:
        return None

    result['rows_affected'] = data.rowcount

    return result
