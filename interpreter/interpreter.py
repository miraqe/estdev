# Prompt user for input
expression = input("Enter an arithmetic expression (e.g. 1 + 1): ")

# Split the input into its constituent parts
parts = expression.split()
if len(parts) != 3:
    print("Error: Invalid input")
    exit()

x, operator, y = parts

# Convert x and y to floats
try:
    x = float(x)
    y = float(y)
except ValueError:
    print("Error: Invalid input")
    exit()

# Perform the appropriate arithmetic operation
if operator == "+":
    result = x + y
elif operator == "-":
    result = x - y
elif operator == "*":
    result = x * y
elif operator == "/":
    result = x / y
else:
    print("Error: Invalid operator")
    exit()

# Output the result as a floating-point value formatted to one decimal place
print("{:.1f}".format(result))
