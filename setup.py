# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='pythonyzbx',
      version='1.0',
      description='some script for yzbx daily life',
      url='http://github.com/yzbx/yzbxLib',
      author='yzbx',
      author_email='youdaoyzbx@163.com',
      license='MIT',
      packages=['pythonyzbx'],
      install_requires=[
          'opencv_python',
      ],
      zip_safe=False)