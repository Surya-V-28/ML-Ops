
## checking for the entire packages in the ML 
from setuptools import find_packages,setup
from typing import List
ls =  ['pandas','numpy','seaborn']


HYPEN_E_DOT ='-e.'
def get_reuirements(paths:str)->List[str]:
    ## thisfunctions will return the listof requirements 
    requirements = []
    with open(paths)  as file_object:
        requirements = file_object.readlines()
        requirements= [ req.replace('/n','') for req in requirements ]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='mlprojects',
    version='0.0.1',
    author='Surya-V',
    author_email='surya.woot.231@gmail.com',
    packages=find_packages(),
    install_requires = get_reuirements('requirements.txt')
)


