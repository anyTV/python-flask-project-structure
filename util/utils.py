import datetime
import hashlib
import io
import json
import math
import random
import time
import urllib
import uuid

SALT = '5a52bf3ae03b415cbb1ff6df1265b019'


def hash(string):
    return hashlib.sha1(str(string)).hexdigest()


def get_data(reqd, optional, body):
    i = len(reqd)
    ret = {}

    i -= 1
    while i >= 0:
        temp = reqd[i]
        if not temp in body or type(body[temp]) == object:
            return str(temp) + ' is missing'
        ret[temp] = body[temp]
        i -= 1

    i = len(optional)

    i -= 1
    while i >= 0:
        temp = optional[i]
        if temp in body:
            ret[temp] = body[temp]
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


def generate_UUID():
    return uuid.uuid4()


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
    if string:
        return ' '.join(string.split()).title()
    return False


def caps_first(string):
    return string[0].upper() + string[1:]


def clean_string(string):
    return ' '.join(string.split())


def split(a, n):
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
        params_encoded.append(urllib.quote(key, safe='~()*!.\'')
                              + '=' + urllib.quote(params.get(key), safe='~()*!.\''))

    return '&'.join(params_encoded)


def nida():
    return hash(SALT + hash(datetime.datetime.now()))


def mida(access_token):
    return hash(SALT + hash(access_token))
