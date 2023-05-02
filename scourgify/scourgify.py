import csv
import sys


def clean_csv(input_file, output_file):
    with open(input_file, "r") as file:
        reader = csv.reader(file)
        rows = [row for row in reader if len(row) == 3]
    with open(output_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python scourgify.py input_file.csv")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = "after.csv"

    try:
        clean_csv(input_file, output_file)
    except FileNotFoundError:
        print("Invalid input file")
        sys.exit(1)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        sys.exit(1)
    else:
        print(f"Successfully cleaned {input_file} to {output_file}")
        sys.exit(0)
