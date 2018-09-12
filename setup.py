from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

setup(
    name='optional.py',
    version='0.1.4',
    description='An implementation of the Optional object in Python',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Chad Befus',
    author_email='crbefus@gmail.com',
    url='https://github.com/cbefus/optional.py',
    license='GNU General Public License (GPL)',
    packages=find_packages(exclude=('test')),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries'
    ],
    keywords='optional datatype library',
    python_requires='>=2.7'
)
