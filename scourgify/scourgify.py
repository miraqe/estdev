import csv
import sys
import os.path

# Check for correct number of arguments
if len(sys.argv) != 3:
    print("Usage: python scourgify.py input.csv")
    sys.exit(1)

# Check that input file exists
if not os.path.isfile(sys.argv[1]):
    print(f"Error: {sys.argv[1]} not found.")
    sys.exit(1)

# Check if output file exists and overwrite if necessary
if os.path.isfile("after.csv"):
    print("Warning: 'after.csv' already exists and will be overwritten.")

# Open input file and read contents
with open(sys.argv[1], newline='') as csvfile:
    reader = csv.reader(csvfile)
    data = [row for row in reader]

# Cleanse data
clean_data = [[cell.strip().replace('\n', ' ') for cell in row] for row in data]

# Write cleansed data to output file
with open("after.csv", "w", newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(clean_data)

print("CSV file has been cleansed and saved as 'after.csv'.")
