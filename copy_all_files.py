#! /usr/bin/python3

# Prompt the user for the source directory and destination directory
# Check if the source directory exists
# Check if the destination directory exists, and if not, create it
# List all files in the source directory
# Iterate through the list of files and copy them to the destination directory
# Copy the file to the destination directory
# Handle error if source doesn't exist


import os
import shutil

# Prompt the user for the source directory and destination directory
source_directory = input("Enter the source directory path: ")
destination_directory = input("Enter the destination directory path: ")

# Check if the source directory exists
if os.path.exists(source_directory) and os.path.isdir(source_directory):
    # Check if the destination directory exists, and if not, create it
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    # List all files in the source directory
    files = os.listdir(source_directory)

    # Iterate through the list of files and copy them to the destination directory
    for file in files:
        source_file = os.path.join(source_directory, file)
        destination_file = os.path.join(destination_directory, file)

        # Check if the source item is a file (not a directory) before copying
        if os.path.isfile(source_file):
            shutil.copy2(source_file, destination_file)

# Handle error if source doesn't exist

    print("Files copied successfully.")
else:
    print(f"The source directory '{source_directory}' does not exist.")






























