from setuptools import setup
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='App Name',
    version='0.1',
    long_description=read('README.md'),
    packages=['app', 'instance', 'lib', 'util'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'sqlalchemy',
        'pymysql',
        'requests',
        'uwsgi',
        'flask-cors',
        'Flask-Mail',
        'Flask'
    ]
)
