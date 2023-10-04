#! /usr/bin/python3


import os
import shutil

# Define the directory name to create
directory_name = "python_scripts"

# Create the directory if it doesn't exist
if not os.path.exists(directory_name):
    os.mkdir(directory_name)

# Get a list of all files in the current directory
current_dir = os.getcwd()
files = os.listdir(current_dir)

# Loop through the files and move .py files to the 'python_scripts' directory
for file in files:
    if file.endswith(".py"):
        shutil.move(file, os.path.join(directory_name, file))

print("Python files moved to 'python_scripts' directory.")

