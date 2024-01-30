#!/usr/bin/python3
import json
import os
import subprocess
from getpass import getuser


from todo.utility import read_json_file
from todo.constants import FileConstants
from todo.constants import ConfigKeys

class Config:
    """Namespace for dealing with .config.json file"""

    # Replace in prod!
    # This is likely to be deprecated eventually. We want the user to specify the 
    # location of the config file, when the setup command is ran.
    CONFIG_FILE_LOCATION = os.path.join(os.path.expanduser("~"), FileConstants.CONFIG)

    def run():
        """Opens the config file"""
        print(Config.CONFIG_FILE_LOCATION)
        subprocess.run(["nano", Config.CONFIG_FILE_LOCATION])

    def exists():
        """Return true if config file exists, otherwise false."""
        return os.path.exists(Config.CONFIG_FILE_LOCATION)

    def create():
        """Create a config file, must be ran before usage of To-Do CLI"""
        new_config = {
            # Default empty string raises file not found error, which is what we want
            ConfigKeys.KEY_CURRENT_TODO: "",
            ConfigKeys.KEY_TODO_NAMES: []
        }

        with open(Config.CONFIG_FILE_LOCATION, "w", encoding="utf-8") as f:
            json.dump(new_config, f, indent=4)

        return Config.CONFIG_FILE_LOCATION

    def set_todo_file(todo_file_path):
        """Set the todo file, that is to be used in the future"""
        data = read_json_file(Config.CONFIG_FILE_LOCATION)

        data[ConfigKeys.KEY_CURRENT_TODO] = todo_file_path

        with open(Config.CONFIG_FILE_LOCATION, "w", encoding="utf-8") as f:
            json.dump(data, f, indent = 4)


    def add_todo_name(todo_file_path):
        """Add a todo file name and path to the config file"""
        data = read_json_file(Config.CONFIG_FILE_LOCATION)

        data[ConfigKeys.KEY_TODO_NAMES].append(todo_file_path)

        with open(Config.CONFIG_FILE_LOCATION, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def get_todo_file_path():
        """Return the todo file path"""
        data = read_json_file(Config.CONFIG_FILE_LOCATION)

        return data[ConfigKeys.KEY_CURRENT_TODO]
    
    def check_todo_existence():
        """Goes through the locations in the config file todo names and sees if they exist."""
        data = read_json_file(Config.CONFIG_FILE_LOCATION)

        data[ConfigKeys.KEY_TODO_NAMES] = [path for path in data[ConfigKeys.KEY_TODO_NAMES] if os.path.isfile(path)]
        
        current_path = data[ConfigKeys.KEY_CURRENT_TODO]
        # "" is default path
        data[ConfigKeys.KEY_CURRENT_TODO] = current_path if os.path.isfile(current_path) else ""

        with open(Config.CONFIG_FILE_LOCATION, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
