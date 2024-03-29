#!/usr/bin/python3

from setuptools import setup

setup(
    name='turnkey-gitwrapper',
    version='0.12',
    description="Py3 wrapper library for working with git directories",
    author='TurnKey GNU/Linux',
    author_email='jeremy@turnkeylinux.org',
    license='GPLv3+',
    url='https://github.com/JedMeister/turnkey-gitwrapper',
    packages=['gitwrapper',],
    package_data={"gitwrapper": ["py.typed"]}
)
