from setuptools import find_packages, setup
from typing import List 

def get_requirements()->List[str]:

    """
        This Functions will return list of requirements
    """

    requirement_list:List[str] = []
    try:
        with open('requirements.txt','r') as file:
            #Read lines from the file 
            lines = file.readlines()
            ## Process each Line
            for line in lines:
                requirement = line.strip()
                ## ignore empty lines and -e .
                if requirement and requirement != "-e .":
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_list


setup(
    
    name = "Network_Security_Project",
    version = "0.0.1",
    author =  "Shivam Vala",
    author_email = "shivamvala122@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()

)
