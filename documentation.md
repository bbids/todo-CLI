# Nomenclature
To-Do/todo file:

    .todo_data.json

config file: 

    .config.json


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

# .config.json
Right now it is created at the current working directory.

To be accessable also via config command in the future.
    


# Create
- automatically sets the current To-Do in config file to the new To-Do

# Reset
- resets the ids of all the task