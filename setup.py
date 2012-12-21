#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup


setup(
    name='django-cachekill',
    version='0.1',
    description='App to kill Django templace cache without a restart',
    author='Becky Lewis',
    long_description=open('README.md', 'r').read(),
    url='http://www.github.com/scaryclam/django-cachekill',
    packages=[
        'cachekill',
    ],
    package_data={
        'cachekill': [
            'templates/*',
        ]
    },
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires=[
        'django>=1.2',
    ],
)
