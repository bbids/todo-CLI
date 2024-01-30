# How this works
There is a config.json file that is shared among all the todo files. 
The script makes use of the config file to know which todo file 
it must access via the current-todo. 

A todo file contains tasks. There can be multiple todo files on the system 
and you can access any of them anywhere. There are some commands such 
as set/get/config that have support for this.

You get the basic add/read/update/remove commands, as well as some supporting 
ones such as reset_ids, config, set and get.

The "cool" feature is the interact mode. Right now it allows for easy 
deletion of tasks. There is potential in the interact mode, 
but a few more improvements are necessary.


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
It is automatically created in the '/home/usr/' folder. It contains the 
locations of all the todo files, which it the script checks if they still 
exist everytime the config command is ran. More importantly it includes the 
current todo file. This allows a user to work with a specific todo file no 
matter where on the system the CLI is currently at. 

## Commands

# config
Opens the config file using nano.

Available are all the locations of the todo files. Using the config command is 
more appropriate than outright using the config file. This is because the 
config command also checks if the paths specified in the config file are valid. 

# create
Automatically sets the current todo todo in config file to the current todo file. 

# reset_ids
Resets the ids of all the task. This may be useful because removing tasks does not 
change the IDs. This is a design decision. The reason is that we don't want to 
confuse the user by automatically updating indeces. Thus by giving them 
control of when to reset them is a fine solution.
