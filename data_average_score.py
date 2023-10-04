#! /usr/bin/python3

import csv

# Specify the column you want to calculate the average for
target_column = 'Score'

try:
    with open('data.csv', mode='r') as file:
        reader = csv.DictReader(file)
        total = 0
        count = 0

        for row in reader:
            try:
                value = float(row[target_column])
                total += value
                count += 1
            except ValueError:
                pass

        if count > 0:
            average = total / count
            print(f"Average {target_column}: {average}")
        else:
            print(f"No valid data found in the {target_column} column.")
except FileNotFoundError:
    print("File 'data.csv' not found.")







