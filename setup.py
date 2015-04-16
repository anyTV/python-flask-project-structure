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
        'Flask>=0.10.1',
        'flask-cors>=1.10.3',
        'requests>=2.5.3',
        'sqlalchemy>=0.9.9',
        'mysql-python>=1.2.5'
    ]
)
