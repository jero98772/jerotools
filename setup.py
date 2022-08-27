#!/usr/bin/env python 
# -*- coding: utf-8 -*-"
"""
jerotools - 2022 - por jero98772
jerotools - 2022 - by jero98772
"""
from setuptools import setup, find_packages
setup(
	name='jerotools',
	version='1.1.0',
	license='GPLv3',
	author_email='jero98772@protonmail.com',
	author='jero98772',
	description='tools i often use',
	url='',
	packages=find_packages(),
    install_requires=['numpy','opencv-python', 'matplotlib','Flask','pandas','deep-translator','cryptography','scipy'],
    include_package_data=True,
)