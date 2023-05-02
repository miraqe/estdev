import csv
import sys
import os.path

# Check for correct number of arguments
if len(sys.argv) != 3:
    print("Usage: python scourgify.py before.csv after.csv")
    sys.exit(1)

# Check that input file exists
if not os.path.isfile(sys.argv[1]):
    print(f"Error: {sys.argv[1]} not found.")
    sys.exit(1)

# Check if output file exists and overwrite if necessary
if os.path.isfile(sys.argv[2]):
    print(f"Warning: '{sys.argv[2]}' already exists and will be overwritten.")

# Open input file and read contents
with open(sys.argv[1], newline='') as csvfile:
    reader = csv.reader(csvfile)
    data = [row for row in reader]

# Cleanse data
clean_data = [[cell.strip().replace('\n', ' ') for cell in row] for row in data]
if len(clean_data[0]) != 3 or clean_data[0][0] != 'first' or clean_data[0][1] != 'last' or clean_data[0][2] != 'house':
    print("Error: CSV file does not have the specified format.")
    sys.exit(1)

# Write cleansed data to output file
with open(sys.argv[2], "w", newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(clean_data)

print(f"CSV file has been cleansed and saved as '{sys.argv[2]}'.")

