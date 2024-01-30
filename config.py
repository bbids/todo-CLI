#!/usr/bin/python3
import json
import os

from utility import read_json_file
from constants import FileConstants
from constants import ConfigKeys

# Replace in prod!
# Add to documentation
# This is likely to be deprecated eventually. We want the user to specify the 
# location of the config file, when the setup command is ran.
CONFIG_FILE_LOCATION = os.path.join(os.getcwd() , FileConstants.CONFIG)

def config_exists():
    """Return true if config file exists, otherwise false."""
    return os.path.exists(CONFIG_FILE_LOCATION)

def config_setup():
    """Create a config file, must be ran before usage of To-Do CLI"""
    # Default empty string raises file not found error, which is what we want
    new_config = {
        ConfigKeys.KEY_CURRENT_TODO: ""
    }

    with open(CONFIG_FILE_LOCATION, "w", encoding="utf-8") as f:
        json.dump(new_config, f, indent=4)

    return CONFIG_FILE_LOCATION

def config_rewrite_current_todo(todo_file_path):
    """Rewrite the current To-Do file location. """
    data = read_json_file(CONFIG_FILE_LOCATION)

    data[ConfigKeys.KEY_CURRENT_TODO] = todo_file_path

    with open(CONFIG_FILE_LOCATION, "w", encoding="utf-8") as f:
        json.dump(data, f)

def config_get_current_todo():
    """Return the current To-Do file location"""
    data = read_json_file(CONFIG_FILE_LOCATION)

    return data[ConfigKeys.KEY_CURRENT_TODO]