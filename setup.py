from setuptools import setup, find_packages

setup(
    name='Music Dashboard',
    version='0.0.4',
    long_description='Music Distribution and Access for Freedom!',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask']
)