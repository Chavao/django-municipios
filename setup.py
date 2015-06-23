import re
from os import path
from setuptools import setup


# read() and find_version() taken from jezdez's python apps, ex:
# https://github.com/jezdez/django_compressor/blob/develop/setup.py

def read(*parts):
    return open(path.join(path.dirname(__file__), *parts)).read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M,
    )
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='django-municipios',
    version=find_version('municipios', '__init__.py'),
    author='ZNC Sistemas',
    author_email='contato@znc.com.br',
    description="""Aplicação plugável Django com modelos e widgets para os Municípios Brasileiros""",
    long_description=read('README.rst'),
    url='https://github.com/znc-sistemas/django-municipios',
    license='MIT',
    packages=[
        'municipios',
        'municipios.migrations',
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: BSD License',
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        'Topic :: Utilities',
        "Framework :: Django",
    ]
)
