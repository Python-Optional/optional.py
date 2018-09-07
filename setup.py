from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='optional.py',
    version='0.1.0',
    description='An implementation of the Optional object in Python',
    long_description=readme,
    author='Chad Befus',
    author_email='crbefus@gmail.com',
    url='https://github.com/cbefus/optional.py',
    license=license,
    packages=find_packages(exclude=('test'))
)
