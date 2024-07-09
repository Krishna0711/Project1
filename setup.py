from setuptools import find_packages,setup

setup(
    name= 'MCQ_Generator',
    version='0.0.1',
    description= 'This file used to donload all the necessary files for this project',
    author='Krishna',
    install_requires = ['openai','langchain','streamlit','python-dotenv','PyPDF2'],
    packages= find_packages()
    )
