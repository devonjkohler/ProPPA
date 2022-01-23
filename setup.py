from setuptools import setup
import os
import sys

_here = os.path.abspath(os.path.dirname(__file__))

if sys.version_info[0] < 3:
    with open(os.path.join(_here, 'README.rst')) as f:
        long_description = f.read()
else:
    with open(os.path.join(_here, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()

version = {}
with open(os.path.join(_here, 'ProPPA', 'version.py')) as f:
    exec(f.read(), version)

setup(
    name='ProPPA',
    version=version['__version__'],
    description='Probabilistic Programming Language for describing continuous-time stochastic systems.',
    long_description=long_description,
    author='Anastasis Georgoulas',
    author_email='temp@example.com',
    url='https://github.com/ageorgou/ProPPA',
    license='MPL-2.0',
    packages=['ProPPA'],
    install_requires=[
        'pyparsing==2.2.2',
        'docopt',
        'numpy',
        'matplotlib'
        ],
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3.6'],
    )