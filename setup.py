"""
QT UI Extension

Author: SF-Zhou
Date: 2016-08-07

See:
https://github.com/sf-zhou/quite
"""

from setuptools import setup, find_packages

setup(
    name='quite',
    version='0.0.1',
    description='QT UI Extension',
    url='https://github.com/sf-zhou/quite',

    author='SF-Zhou',
    author_email='sfzhou.scut@gmail.com',

    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    keywords='qt ui',
    packages=find_packages(exclude=['docs', 'tests']),
    install_requires=['st', 'prett']
)
