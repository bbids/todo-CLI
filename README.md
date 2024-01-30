Practical To-Do task manager for the command line.

Supports JSON file format for the non-volatile storage of tasks.

Work in progress.

# Install
We use python setuptools.

    pip install .

# Usage
First create a todofile.

    todo create

Then you can add, read, update and remove

    todo add "This is some content" --prio 5

    todo read

    todo update 0 --cont "Updating a task with ID 0. IDs are printed on read" --prio  3

    todo remove 0

You can reset ID's. It starts with topmost task and assigns it an ID 0, then it increments at every task. This is useful because removing doesn't reset IDs.

    todo reset_ids

There is also an interact mode. 

    todo interact

You can move using keys 'w' for up, and 's' for down.

You can delete using a key 'd'.

# set and get
Use set command with a dot to set the working directory's todo file as focused.

    todo set .

You can also use an absolute path as well. 

Use get command to get the location of the todo file being focused at the moment.

    todo get

# Config
The config file can be accessed via:

    todo config

# Interact mode
![Interactive mode](https://github.com/bbids/To-Do-CLI/blob/master/ss.png)

# More?
See the documentation.md

# Help  
    todo -h

# Testing
Right now, for development reasons, testing is conducted in the tests folder  
    
    python3 testHappyPath.py
