# This file make the entire ML project to run as one package. Jusnt similar to other packages like seaborn, Pandas ,Sklearn
from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function will returns the list of requirements
    '''
    requirements=[]
    
    with open(file_path) as file_obj :
        requirements=file_obj.readlines()
        requirements=[line.replace('\n','') for line in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Balaji',
    author_email='balajir2312@gmail.com',
    packages=find_packages(), 
    install_requires=get_requirements('requirements.txt')
    
)

'''
find_packages- Find the packages that are required to execute.[It will search for __init__.py file and build that package. So that we can 
import it and use it like pandas and numpy ] 
install_requires-What are the libraries required to be installed initially.
'''
