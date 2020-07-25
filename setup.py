# -*- coding: utf-8 -*-

"""
@date: 2020/7/25 下午7:33
@file: setup.py.py
@author: zj
@description: 
"""

import setuptools
import os
import shutil
import sys


class UploadCommand(setuptools.Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            here = os.path.abspath(os.path.dirname(__file__))
            self.status('Removing previous builds…')
            shutil.rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPI via Twine…')
        os.system('twine upload dist/*')

        self.status('Pushing git tags…')
        os.system('git tag v{0}'.format(get_version()))
        os.system('git push --tags')

        sys.exit()


def get_version():
    init_py_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "python_setup", "__init__.py")
    init_py = open(init_py_path, "r").readlines()
    version_line = [l.strip() for l in init_py if l.startswith("__version__")][0]
    version = version_line.split("=")[-1].strip().strip("'\"")

    return version


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-setup",  # Replace with your own username
    version=get_version(),
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
    entry_points={
        'console_scripts': [
            'print_hello = python_setup.tools.cli:main'
        ]
    },
    cmdclass={
        'upload': UploadCommand,
    },
)
