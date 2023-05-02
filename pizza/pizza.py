import sys
import csv
from tabulate import tabulate

if len(sys.argv) != 2 or not sys.argv[1].endswith('.csv'):
    sys.exit('Usage: python pizza.py file.csv')

try:
    with open(sys.argv[1], newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        data = [row for row in reader]
except FileNotFoundError:
    sys.exit('File does not exist')
except csv.Error:
    sys.exit('Not a CSV file')

print(tabulate(data, headers=headers, tablefmt='grid'))
