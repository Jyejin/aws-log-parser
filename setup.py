#!/usr/bin/env python

import pathlib
from setuptools import setup

setup(
    name='aws-log-parser',
    version='1.3.1',
    description='Python module for parsing AWS CloudFront and LoadBalancer logs',
    long_description=(pathlib.Path(__file__).parent / 'README.md').read_text(),
    long_description_content_type='text/markdown',
    url='https://github.com/dpetzold/aws-log-parser',
    author='Derrick Petzold',
    author_email='github@petzold.io',
    license='Apache',
    packages=[
        'aws_log_parser',
    ],
    install_requires=[
        'python-geoip@git+https://github.com/maxamante/python-geoip.git',
        'python-geoip-geolite2==2015.303',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
        'pytest-cov',
    ],
)
