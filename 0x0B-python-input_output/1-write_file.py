#!/usr/bin/python3
"""Defines a file-writing function."""

def write_file(filename="", text=""):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            num_chars_written = file.write(text)
        return num_chars_written
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return 0 