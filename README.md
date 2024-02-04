Practical To-Do task manager for the command line.  

Built with Python, use SQLite for storage.

# Install
We use python setuptools.

    pip install .

# Usage
You can add, read, update and remove

    todo add "This is some content" --prio 5

    todo read

    todo update 0 --cont "Updating a task with ID 0. IDs are printed on read" --prio  3

    todo remove 0

# Old todo
Checkout old-todo branch. There's no database there, it uses JSON files. It does however have more features such as interactive mode.