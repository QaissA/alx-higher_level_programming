#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys

import json
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def add_arguments_to_list_and_save(*args):
    filename = "add_item.json"

    if os.path.exists(filename):
        data = load_from_json_file(filename)
        if not isinstance(data, list):
            data = []
    else:
        data=[]
    data.extend(args)

    save_to_json_file(data, filename)

if __name__ == "__main__":
    
    import sys
    args = sys.argv[1:]

    add_arguments_to_list_and_save(*args)

