#!/bin/env python3

"""
__date__ = '2023-10-08'
__author__ = 'liulin4@genomics.cn'
"""

import sys
from setuptools import setup, find_packages
from pathlib import Path

_version_ = "1.0.0"


setup(
    name = "DeepST",
    version = _version_,
    author="liulin4",
    author_email = "liulin4@genomics.cn",
    description = "Identifying spatial domains",
    keywords=["Spatial_transcriptomics", "stereo-seq", "bioinformatics"],
    packages = find_packages(),
    classifiers = [
        'Programming Language :: Python :: 3.9'
        'Environment :: Console'
    ],
    install_requires = [
    ]
)


