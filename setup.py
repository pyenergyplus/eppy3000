#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ["munch", ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Santosh Philip",
    author_email='santosh@noemail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        'Natural Language :: English',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="E+ scripting using epJSON file format",
    install_requires=requirements,
    license="Mozilla Public License, v. 2.0",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='eppy3000',
    name='eppy3000',
    packages=find_packages(include=['eppy3000']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/pyenergyplus/eppy3000',
    version='0.1.1',
    zip_safe=False,
)
