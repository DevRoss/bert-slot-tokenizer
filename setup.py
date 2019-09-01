#!/usr/bin/env python
# -*- coding: utf-8 -*-

# For a fully annotated version of this file and what it does, see
# https://github.com/pypa/sampleproject/blob/master/setup.py

# To upload this file to PyPI you must build it then upload it:
# python setup.py sdist bdist_wheel  # build in 'dist' folder
# python-m twine upload dist/*  # 'twine' must be installed: 'pip install twine'


import ast
import io
import os
import re

from setuptools import find_packages, setup

DEPENDENCIES = []
EXCLUDE_FROM_PACKAGES = ["contrib", "docs", "tests*"]
CURDIR = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(CURDIR, "README.md"), "r", encoding="utf-8") as f:
    README = f.read()


def get_version():
    main_file = os.path.join(CURDIR, "bert_slot_tokenizer", "main.py")
    _version_re = re.compile(r"__version__\s+=\s+(?P<version>.*)")
    with io.open(main_file, "r", encoding="utf8") as f:
        match = _version_re.search(f.read())
        version = match.group("version") if match is not None else '"unknown"'
    return str(ast.literal_eval(version))


setup(
    name="bert_slot_tokenizer",
    version=get_version(),
    author="DevRoss",
    author_email="devross1997@gmail.com",
    description="A tool for converting raw text to slot",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/DevRoss/bert-slot-tokenizer",
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    include_package_data=True,
    keywords=['bert_slot_tokenizer', 'bert', 'slot filling'],
    scripts=[],
    entry_points={"console_scripts": ["bert_slot_tokenizer=bert_slot_tokenizer.main:main"]},
    zip_safe=False,
    install_requires=DEPENDENCIES,
    test_suite="tests.test_project",
    python_requires=">=2.7",
    # license and classifier list:
    # https://pypi.org/pypi?%3Aaction=list_classifiers
    license="License :: OSI Approved :: Apache Software License",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: Implementation :: PyPy"
    ],
)
