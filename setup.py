#!/usr/bin/env python

VERSION='0.0.01'

from setuptools import setup

tests_require = [
  'nose==1.3.7',
  'Paste==2.0.2',
]

install_requires = [
  'requests==2.2.1',
  'web.py==0.37',
]

if __name__ == '__main__':
  setup(
    name='taskcluster-api',
    version=VERSION,
    description='Web api for tracking build statuses',
    author='Clayton Kehoe',
    author_email='clayton.kehoe@outlook.com',
    url='https://github.com/ckehoe/taskcluster-api',
    install_requires=install_requires,
    test_suite="nose.collector",
    tests_require=tests_require,
    zip_safe=False,
  )
