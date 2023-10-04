#! /usr/bin/python3

import csv

# Sample data with two columns
data = [
    ['Alice', 85],
    ['Bob', 92],
    ['Charlie', 78],
    ['David',95]
]

# Open the CSV file for writing in 'w' mode
with open('data.csv', mode='w') as file:
    # Create a CSV writer object
    writer = csv.writer(file)

    # Write header (optional)
    writer.writerow(['Name', 'Score'])

    # Write multiple rows of data with two columns
    writer.writerows(data)

# File is automatically closed when you exit the 'with' block

