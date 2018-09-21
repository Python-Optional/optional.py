from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

setup(
    name='optional.py',
    version='0.2.2',
    description='An implementation of the Optional object in Python',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Chad Befus',
    author_email='crbefus@gmail.com',
    url='https://github.com/cbefus/optional.py',
    license='MIT License',
    packages=find_packages(exclude=('test')),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries'
    ],
    keywords='optional datatype library',
    python_requires='>=2.7'
)
