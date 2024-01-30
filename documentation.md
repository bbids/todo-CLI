#How this works
There is a config.json file. This one is shared among all the todo files. Right now it includes information about the current todo file being worked on. This will allow the project to be more flexible when the package is used as a command.

Additional configurations may be added in the future to the config file.

The todo file includes tasks, you can see a sample task below.

Next development goal is to finish the first version of the To-Do CLI program. That version should be easy to use via a command.



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
