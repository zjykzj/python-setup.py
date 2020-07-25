# -*- coding: utf-8 -*-

"""
@date: 2020/7/25 下午7:34
@file: cli.py
@author: zj
@description: 
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-setup",  # Replace with your own username
    version="0.0.1",
    author="zj",
    author_email="wy163zhuj@163.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zjZSTU/python-setup.py.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
