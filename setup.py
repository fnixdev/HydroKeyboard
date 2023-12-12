from os import path
from setuptools import setup


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='hydrokeyboard',
    version='0.1.5',
    author='PyMaster',
    author_email='',
    description='Best Keyboard and Pagination for the hydrogram Library.',
    license='MIT',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet',
        'Topic :: Communications',
        'Topic :: Communications :: Chat',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords='telegram hydrogram keyboard bot userbot',
    url='https://github.com/fnixdev/hydrokeyboard',
    packages=['hydrokeyboard'],
    install_requires=['hydrogram', 'tgcrypto'],
    long_description=long_description,
    long_description_content_type='text/markdown',
)
