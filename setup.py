#!/usr/bin/env python

from setuptools import setup
import doctest

MODULE = 'azlike_ruby'

tests = lambda: doctest.DocTestSuite(MODULE)

setup(
    name=MODULE,
    version='1.0',
    author='mugwort_rc',
    author_email='mugwort _dot_ rc _at_ gmail com',
    description='Ruby extension for Python-Markdown.',
    long_description_markdown_filename='README.md',
    url='https://github.com/mugwort-rc/' + MODULE,
    py_modules=[MODULE],
    test_suite='setup.tests',
    install_requires=['Markdown'],
    license='The BSD 2-Clause License',
    keywords='markdown ruby',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: The BSD 2-Clause License (BSD)',
        'Environment :: Web Environment',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Message Boards',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: News/Diary',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML'
    ]
)
