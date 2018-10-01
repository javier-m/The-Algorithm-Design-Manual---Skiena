import os

from setuptools import find_packages, setup


package_path = os.path.dirname(os.path.abspath(__file__))


def dependencies():
    """
    Obtain the dependencies from requirements.txt.
    """
    with open(os.path.join(package_path, 'requirements.txt')) as reqs:
        return reqs.read().splitlines()


setup(
    name='datastructures',
    description='data structures',
    author='Xavier Martinet',
    packages=find_packages(exclude=['tests']),
    install_requires=dependencies(),
)
