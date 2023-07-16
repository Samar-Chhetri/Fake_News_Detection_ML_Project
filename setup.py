from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name= 'Fake_News_Detection_ML_Project',
    version= '0.0.1',
    long_description='A simple machine learning model to predict whether a news is fake or not.',
    author= 'Samar Chhetri',
    author_email= 'samarchhetri23@gmail.com',
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')
)