#! /usr/bin/python3


import shutil
import os

'''source_directory = '/path/to/source_directory'  # Source directory path
destination_directory = '/path/to/destination_directory'  # Destination directory path
file_extension = '.txt'  # Desired file extension

try:
    for filename in os.listdir(source_directory):
        if filename.endswith(file_extension) and os.path.isfile(os.path.join(source_directory, filename)):
            shutil.copy(os.path.join(source_directory, filename), os.path.join(destination_directory, filename))
            print(f"File '{filename}' copied successfully.")
except FileNotFoundError:
    print("Source or destination directory not found.")

'''

# Get user input for the source directory
source_directory = input("Enter the source directory path: ")

# Get user input for the destination directory
destination_directory = input("Enter the destination directory path: ")

file_extension = '.txt'  # Desired file extension

try:
    for filename in os.listdir(source_directory):
        if filename.endswith(file_extension) and os.path.isfile(os.path.join(source_directory, filename)):
            shutil.copy(os.path.join(source_directory, filename), os.path.join(destination_directory, filename))
            print(f"File '{filename}' copied successfully.")
    print("Copy operation completed.")
except FileNotFoundError:
    print("Source or destination directory not found.")


























