# Prompt user for input
expression = input("Enter an arithmetic expression (e.g. 1 + 1): ")

# Split the input into its constituent parts
x, operator, y = expression.split()

# Convert x and y to floats
x = float(x)
y = float(y)

# Perform the appropriate arithmetic operation
if operator == "+":
    result = x + y
elif operator == "-":
    result = x - y
elif operator == "*":
    result = x * y
elif operator == "/":
    result = x / y

# Output the result as a floating-point value formatted to one decimal place
print("{:.1f}".format(result))
