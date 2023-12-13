from setuptools import find_packages,setup
from typing import List


def get_requirements(file_path:str) -> List[str]:

    '''
        This function will return a list of libraries / packages required to run the application
    '''
    e = '-e .'
    with open(file_path) as file:
        requirements = file.readline()
        requirements = [req.replace("\n","") for req in requirements]
        
        if e in requirements:
            requirements.remove(e)

    return requirements

setup(

    name = 'MLProject',
    version = '0.1',
    author = 'HSSASSA',
    author_email ='abdelilah.hssassa@etu.uae.ac.ma',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')

)