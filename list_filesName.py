#! /usr/bin/python3

import os

# Prompt the user for the directory path
directory_path = input("Enter the directory path: ")

# Check if the directory exists
if os.path.exists(directory_path) and os.path.isdir(directory_path):
    # List all files in the directory
    files = os.listdir(directory_path)

    # Iterate through the list of files and print their names
    for file in files:
        print(file)
else:
    print(f"The directory '{directory_path}' does not exist.")


















