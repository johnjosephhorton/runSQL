#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from os.path import join, dirname

import runSQL 

setup(name='runSQL',
      version = runSQL.__version__,
      author = runSQL.__author__ , 
      author_email = runSQL.__email__,
      url = 'http://github.com/johnjosephhorton/runSQL',
      packages = [''],
      package_dir= {'':'.'}, 
      entry_points={
          'console_scripts':
              ['runSQL = runSQL:main',
               ]}, 
      classifiers=(
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Environment :: Web Environment',
          'License :: OSI Approved :: GNU General Public License v3 or '
          'later (GPLv3+)',
          'Natural Language :: English',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
      ),
      install_requires=['argparse>=1.2.1','psycopg2>=2.4.5'],
      )

