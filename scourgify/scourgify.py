import csv
import sys

# Check for correct usage
if len(sys.argv) != 3:
    print("Usage: python scourgify.py input_file.csv")
    sys.exit(1)

# Check that input file exists
try:
    with open(sys.argv[1], "r") as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
except FileNotFoundError:
    print(f"{sys.argv[1]} not found.")
    sys.exit(1)

# Create the output file
with open("after.csv", "w", newline="") as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(header)

    # Iterate over each row of the input file
    for row in csvreader:
        # Clean up the data
        for i, item in enumerate(row):
            if isinstance(item, str):
                row[i] = item.strip().title()

        # Write the cleaned row to the output file
        csvwriter.writerow(row)

# Check that output file has correct format
try:
    with open("after.csv", "r") as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        if header != ["First Name", "Last Name", "Email", "Phone"]:
            print("Output file does not have specified format.")
            sys.exit(1)
except FileNotFoundError:
    print("Output file not found.")
    sys.exit(1)

print("CSV file cleaned successfully!")
