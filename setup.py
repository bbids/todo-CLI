from setuptools import setup

setup(
    name='To-Do CLI',
    version='1.0.0',
    packages=['src.todo'],
    entry_points={
        'console_scripts': [
            'todo = src.todo:main' 
        ]
    },
)