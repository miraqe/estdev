import csv
import sys

# Check that the user provided exactly two command-line arguments
if len(sys.argv) != 3:
    sys.exit("Usage: python scourgify.py input.csv output.csv")

# Attempt to open the input file for reading
try:
    with open(sys.argv[1], newline='') as input_file:
        reader = csv.DictReader(input_file)
        rows = list(reader)
except FileNotFoundError:
    sys.exit(f"Error: File '{sys.argv[1]}' not found.")

# Convert each name into separate first and last name columns
for row in rows:
    name = row["name"]
    last, first = name.split(", ")
    row["first"] = first
    row["last"] = last
    del row["name"]

# Attempt to open the output file for writing and write the rows to it
try:
    with open(sys.argv[2], "w", newline='') as output_file:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
except PermissionError:
    sys.exit(f"Error: Permission denied when writing to file '{sys.argv[2]}'")
except:
    sys.exit("An unknown error occurred.")
