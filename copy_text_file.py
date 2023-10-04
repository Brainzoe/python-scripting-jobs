#! /usr/bin/python3


try:
    with open('input.txt', 'r') as input_file:
        content = input_file.read()

    with open('output.txt', 'w') as output_file:
        output_file.write(content)

    print("File copied successfully.")
except FileNotFoundError:
    print("File 'input.txt' not found.")





