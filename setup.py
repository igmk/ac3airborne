# setup.py
from distutils.core import setup
from setuptools import find_packages

setup(
  name='ac3airborne',
  packages=find_packages(),
  version='v0.0.6-alpha',
  description='Common utilities for analysing data from the ACLOUD, AFLUX and MOSAiC-ACA airborne campaigns',
  long_description=open('README.md').read(),
  long_description_content_type='text/markdown',
  author='Mario Mech',
  author_email='mario.mech@uni-koeln.de',
  license='MIT-license',
  url='https://github.com/igmk/pyac3airborne',
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  python_requires='>=3',
  install_requires=[
    "requests",
    "pyyaml",
    "intake!=0.6.1",  # due to lacking jinja2 dependency
    "aiohttp",  # required by intake to access catalogs via http
    "intake_xarray",
    "netCDF4",
    "h5netcdf"
  ]
)
