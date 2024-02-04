from setuptools import setup

setup(
    name='To-Do CLI',
    version='1.0.0',
    packages=['todo'],
    entry_points={
        'console_scripts': [
            'todo = todo.main:main' 
        ]
    },
)