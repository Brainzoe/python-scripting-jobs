#! /usr/bin/python3


import os

current_directory = os.getcwd()
print("Files:")
for filename in os.listdir(current_directory):
    if os.path.isfile(os.path.join(current_directory, filename)):
        print(filename)

print("\nDirectories:")
for dirname in os.listdir(current_directory):
    if os.path.isdir(os.path.join(current_directory, dirname)):
        print(dirname)




