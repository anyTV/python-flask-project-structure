# Import core libraries
from lib import database
from lib.error_handler import FailedRequest

# Other imports
from urllib.parse import quote
import hashlib
import json
import math
import random
import re
import string
import time
import uuid
from datetime import datetime

SALT = 'salt'

SPECIAL_CHARACTERS = '[\+\-\=\>\<\!\(\)\{\}\[\]\^\"\~\*\?\:\\\/\ ]|(\&\&)|(\|\|)'


def hash(string):
    return hashlib.sha1(str(string).encode('utf-8')).hexdigest()


def get_data(reqd, optional, body):
    ret = {}

    i = len(reqd) - 1
    while i >= 0:
        temp = reqd[i]

        if not temp in body or type(body[temp]) == object:
            raise FailedRequest(
                'Missing required parameter: ' + str(temp), 400)

        ret[temp] = body[temp]

        if isinstance(ret[temp], str):
            ret[temp] = clean_string(ret[temp])

            if ret[temp] == '':
                raise FailedRequest(
                    'Missing required parameter: ' + str(temp), 400)

        i -= 1

    i = len(optional) - 1
    while i >= 0:
        temp = optional[i]

        if not temp in body or type(body[temp]) == object:
            ret[temp] = None

        else:
            ret[temp] = body[temp]

        if isinstance(ret[temp], str):
            ret[temp] = clean_string(ret[temp])

            if ret[temp] == '':
                ret[temp] = None

        i -= 1

    return ret


def random_string(i):
    possible = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    string = ''
    l = i or 32

    l -= 1
    while l >= 0:
        string += possible[math.trunc(-(-(random.random() * 62) - 1) - 1)]
        l -= 1

    return string


def generate_id(size=6, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def generate_UUID():
    return str(uuid.uuid4())


def unique_short_string(n):
    result = ''
    num = math.trunc(time.time() * random.random())

    while num > 0:
        result = '0123456789abcdefghijklmnopqrstuvwxyz'[num % 36] + result
        num /= 36

    return result.replace('.', '')[0:n]


def pad(num, size):
    return ('000000000' + str(num))[-(size or 2):]


def to_title_case(string):
    return clean_string(string).title()


def caps_first(string):
    return string[0].upper() + string[1:]


def clean_string(string, delimiter=' '):
    return delimiter.join(string.split())


def split(string, delimiter=None):
    if string:
        return string.split(delimiter)

    return []


def divide(a, n):
    length = len(a)
    out = []

    i = 0
    while i < length:
        temp = i
        i += int(math.ceil((length - i) / float(n)))
        out.append(a[temp: i])
        n -= 1

    return out


def slice(a, n):
    length = len(a)
    out = []
    number_of_slice = int(math.ceil(length / float(n)))

    i = 0
    while number_of_slice > 0:
        a = a[i:n]
        out.append(a)
        i += n
        number_of_slice -= 1

    return out


def extend(obj, source):
    for prop in source:
        if hasattr(source, prop):
            obj[prop] = source[prop]

    return obj


def clone(obj):
    return json.loads(json.dumps(obj))


def encode_params(params):
    params_encoded = []

    for key in params.keys():
        params_encoded.append(quote(key, safe='~()*!.\'')
                              + '=' + quote(params.get(key), safe='~()*!.\''))

    return '&'.join(params_encoded)


def nida():
    return hash(SALT + hash(datetime.now()))


def mida(access_token):
    return hash(SALT + hash(access_token))


def has_scopes(db, user_id, *scopes):
    data = database.get(
        db.music_db, 'SELECT * FROM user_scopes WHERE user_id = :user_id AND \
        scope IN :scopes', {'user_id': user_id, 'scopes': scopes})

    return data if len(data) == len(scopes) else None


def generate_filename(_filename):
    filename = _filename.rsplit('.', 1)

    return hash(filename[0]) + '.' + filename[1]


def seconds_to_time(_seconds):
    hours = str(_seconds / 3600.0).split('.')
    hours[1] = '0.' + hours[1]

    minutes = str(float(hours[1]) * 60.0).split('.')
    minutes[1] = '0.' + minutes[1]

    seconds = int(round(float(minutes[1]) * 60.0))
    minutes = int(minutes[0])
    hours = int(hours[0])

    return '{0:02d}:{1:02d}:{2:02d}'.format(hours, minutes, seconds)


def sql_data_to_json(data):

    def date_handler(obj):
        return obj.isoformat() if hasattr(obj, 'isoformat') else obj

    return json.dumps(data, default=date_handler).replace('\'', '\\\'')


def update_pagination_params(config, params):
    params.update({
        'page': int(params['page'] or 1),
        'limit': int(params['limit'] or config['PAGE_LIMIT'])
    })

    return params


def get_pagination_results(params, data):
    result = {
        'total': data['total'],
        'pages': int(math.ceil(float(data['total']) / params['limit'])),
        'results': data['results']
    }

    return result


def replace_special_characters(match_object):
    return '\\' + match_object.group(0)


def es_escape(string):
    return re.sub(SPECIAL_CHARACTERS, replace_special_characters, string)


def log(message):
    print(str(datetime.now()) + ': ' + message)
