#How this works
There is a config.json file. This one is shared among all the todo files. The script makes use of the config file to know which todo file it must access via the current-todo. 

Additional configurations may be added in the future to the config file.

The todo file includes tasks, you can see a sample task below.



# Nomenclature
To-Do/todo file:

    .todo_data.json

config file: 

    .config_data.json


# Priority Levels
- Priority 1: Critical
- Priority 2: Important
- Priority 3: Necessary
- Priority 4: Non-urgent
- Priority 5: Optional  

Other priorities have no default meaning assosiated with them.

# Task format
    sample_task = {
        "ID": id,
        "Priority": priority,
        "Content": content,
        "DueDate": None,
        "Category": None,
    }

# .todo_data.json
Default To-Do file looks like this  

    {
        tasks: []
    }

# .config_data.json
It is automatically created in the '/home/usr/' folder. It contains the locations of all
the todo files, which it the script checks if they still exist everytime the config command
is ran. More importantly it includes the current todo file. This allows a user to work with
a specific todo file no matter where on the system the CLI is currently at. 

## Commands

# config
Opens the config file using nano.

# create
Automatically sets the current todo todo in config file to the new todo file.

# reset_ids
Resets the ids of all the task
