"""
QT UI Extension

Author: SF-Zhou
Date: 2016-08-07

See:
https://github.com/sf-zhou/quite
"""

from setuptools import setup, find_packages
import os
import subprocess


def get_git_latest_tag():
    def _minimal_ext_cmd(cmd: str):
        # construct minimal environment
        env = {}
        for k in ['SYSTEMROOT', 'PATH']:
            v = os.environ.get(k)
            if v is not None:
                env[k] = v
        # LANGUAGE is used on win32
        env['LANGUAGE'] = 'C'
        env['LANG'] = 'C'
        env['LC_ALL'] = 'C'
        out = subprocess.Popen(cmd.split(" "), stdout=subprocess.PIPE, env=env).communicate()[0]
        return out

    try:
        out = _minimal_ext_cmd("git describe --abbrev=0 --tags")
        git_tag = out.strip().decode('ascii')
        # 去除tag中的v/V
        if str(git_tag).startswith("v") or str(git_tag).startswith("V"):
            git_tag = str(git_tag)[1:]
    except OSError:
        git_tag = None

    return git_tag


latest_tag = get_git_latest_tag()
if latest_tag is None:
    print("get_git_latest_tag return None")
    exit(1)

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
    with open('README.md', encoding="utf-8") as f:
        return f.read()


print("use latest tag as version: {}".format(latest_tag))
print("use requirements.txt as install_requires: {}".format(req_list))

setup(
    name='quite',
    version=latest_tag,
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
    install_requires=req_list,
)
