"""Setup script for fixfonts.
"""
from setuptools import setup
from codecs import open
from os import path

VERSION = "1.0.0"
DESCRIPTION = "Removes width inconsistency in fonts, enabling their use in Windows tools like PuTTY"

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as filein:
    long_description = filein.read()

with open(path.join(here, "requirements.txt"), encoding="utf-8") as filein:
    requirements = [line.strip() for line in filein.readlines()]

setup(
    name="fixfonts",
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    url="https://github.com/scott-hand/fix-fixed-fonts",
    author="Scott Hand",
    author_email="scott@vkgfx.com",
    classifiers=["Development Status :: 4 - Beta",
                 "Intended Audience :: Developers",
                 "Programming Language :: Python :: 2"],
    packages=["fixfonts"],
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "fixfonts=fixfonts.app:main"
        ]
    }
)
