"""
    Project Set Up
"""
from setuptools import setup

from _project import NAME, VERSION, LICENSE, DESCRIPTION, URL, PACKAGES, REQUIRES

setup(
    name = NAME,
    version = VERSION,
    license = LICENSE,
    description = DESCRIPTION,
    url = URL,
    packages = PACKAGES,
    install_requires = REQUIRES,
)
