#!/usr/bin/python3
import json
import os

from utility import read_json_file
from constants import FileConstants
from constants import ConfigKeys

class Config:
    """Namespace for dealing with .config.json file"""

    # Replace in prod!
    # This is likely to be deprecated eventually. We want the user to specify the 
    # location of the config file, when the setup command is ran.
    CONFIG_FILE_LOCATION = os.path.join(os.getcwd() , FileConstants.CONFIG)

    def exists():
        """Return true if config file exists, otherwise false."""
        return os.path.exists(Config.CONFIG_FILE_LOCATION)

    def create():
        """Create a config file, must be ran before usage of To-Do CLI"""
        # Default empty string raises file not found error, which is what we want
        new_config = {
            ConfigKeys.KEY_CURRENT_TODO: ""
        }

        with open(Config.CONFIG_FILE_LOCATION, "w", encoding="utf-8") as f:
            json.dump(new_config, f, indent=4)

        return Config.CONFIG_FILE_LOCATION

    def set_todo_file(todo_file_path):
        """Set the todo file, that is to be used in the future"""
        data = read_json_file(Config.CONFIG_FILE_LOCATION)

        data[ConfigKeys.KEY_CURRENT_TODO] = todo_file_path

        with open(Config.CONFIG_FILE_LOCATION, "w", encoding="utf-8") as f:
            json.dump(data, f)

    def get_todo_file_path():
        """Return the todo file path"""
        data = read_json_file(Config.CONFIG_FILE_LOCATION)

        return data[ConfigKeys.KEY_CURRENT_TODO]
