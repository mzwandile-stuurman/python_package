from setuptools import setup, find_packages

setup(
    name="mypackage",
    version='0.1',
    packages=find_packages(exclude='tests*'),
    license='MIT',
    description='EDSA example python package',
    long_description=open('readMe.md').read(),
    install_requires=['numpy'],
    url='https://github.com/mzwandile-stuurman/Top-Scores',
    author="Mzwandile",
    author_email="stuurmanmzwandile@gmail.com"
)