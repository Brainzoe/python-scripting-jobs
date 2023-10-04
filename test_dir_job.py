#! /usr/bin/python3

import os, shutil

file_path = "./my_test_dir"

file_ex = []

def get_file_extension():

    for files in os.listdir(file_path):
        index = files.rfind(".")+1
        if files[index:] not in file_ex:
            file_ex.append(files[index:])

def make_dir():
    for ext in file_ex:
        new_dir_path = os.path.join(file_path, ext)
        if not os.path.exists(new_dir_path):
            os.mkdir(new_dir_path)


def move_files():
    for files in os.listdir(file_path):
        for ext in file_ex:
            new_location = os.path.join(file_path, ext)
            if files.endswith("." + ext):
                old_path = os.path.join(file_path, files)
                new_file_path = os.path.join(new_location, files)
                shutil.move(old_path, new_file_path)


def main():
    get_file_extension()
    make_dir()
    move_files()
print("files sort successfully in", file_path)
main()
