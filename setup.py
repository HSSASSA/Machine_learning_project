from setuptools import find_packages,setup

setup(

    name = 'MLProject',
    version = '0.1',
    author = 'HSSASSA',
    author_email ='abdelilah.hssassa@etu.uae.ac.ma',
    packages = find_packages(),
    install_requires = ['pandas','numpy','seaborn']

)