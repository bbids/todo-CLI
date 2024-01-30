import logging
import sys
import json

def get_data(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        logging.error("Trouble decoding the json file. Exiting ...")
        sys.exit()
    except FileNotFoundError:
        logging.error("File not found. Make sure the path is specified correctly.")
        sys.exit()

    return data   