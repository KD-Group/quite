"""
QT UI Extension

Author: SF-Zhou
Date: 2016-08-07

See:
https://github.com/sf-zhou/quite
"""

from setuptools import setup, find_packages
from version import get_git_version
import os

# 读取项目下的requirements.txt
req_txt_path = os.path.join(os.path.dirname(__file__), "requirements.txt")
if os.path.exists(req_txt_path):
    with open(req_txt_path) as f:
        req_list = f.readlines()
    req_list = [x.strip() for x in req_list]
else:
    req_list = []


def readme():
    """读取README.md文件"""
    with open('readme.md', encoding="utf-8") as f:
        return f.read()


print("use latest tag as version: {}".format(get_git_version()))
print("use requirements.txt as install_requires: {}".format(req_list))

setup(
    name='quite',
    version=get_git_version(),
    description='QT UI Extension',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/KD-Group/quite',

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
    packages=find_packages(exclude=['docs', 'tests', 'examples']),
    include_package_data=True,
    install_requires=req_list,
)
