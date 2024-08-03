#We use setup.py so we can make our model available as a library and we can use it at any device
from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements] # This is for the purpose of replacing /n as we move to the next line
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name= 'mlproject',
    version='0.0.1',
    author='gaurav',
    author_email='ojhagaurav22@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),

)