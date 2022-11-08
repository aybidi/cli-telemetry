from setuptools import setup, find_packages

setup(
    name='filesys',
    version='0.1.0',
    py_modules=['filesys'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'filesys = filesys:cli',
        ],
    },
)