"""Package setup.py script using pbr.

See https://docs.openstack.org/pbr/latest/user/using.html
"""
from setuptools import setup

setup(
    setup_requires=['pbr'],
    pbr=True,
)
