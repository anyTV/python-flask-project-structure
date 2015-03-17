# Import global context
from sqlalchemy     import create_engine
from sqlalchemy.sql import text
from sqlalchemy.orm import sessionmaker, scoped_session


def sql_alchemy_format(_config):
    return 'mysql://' + _config['user'] + ':' + _config['password'] + '@' + \
        _config['host'] + ':' + str(_config['port']) + '/' + _config['db']


# Creates an engine
def make_engine(_config):
    en = create_engine(sql_alchemy_format(_config))
    return en.connect()


# Creates an engine with session based scoping
def make_engine_with_session(_config):
    en      = create_engine(sql_alchemy_format(_config))
    Session = sessionmaker(bind = en)
    return scoped_session(Session)


# Executes db get
def get(_connection, _query, _params):
    result  = []
    
    data = _connection.execute(text(_query), _params)

    for row in data:
        result.append(dict(row) or row)

    _connection.close()
    return result


# Executes raw query
def query(_connection, _query, _params):
    res = {}
    data = _connection.execute(text(_query), _params)
    _connection.commit()

    res['rows_affected'] = data.rowcount
    _connection.close()

    return res

