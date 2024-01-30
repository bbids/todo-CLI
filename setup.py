from setuptools import setup

setup(
    name='To-Do CLI',
    version='1.0.0',
    packages=['todo', 'tests'],
    entry_points={
        'console_scripts': [
            'todo = todo.main:main' 
        ]
    },
    install_requires=["getch"],
)