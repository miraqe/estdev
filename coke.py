# Define the price of a bottle of Coke
PRICE = 50

# Define the valid denominations
DENOMINATIONS = [25, 10, 5]

# Initialize the total amount inserted by the user and the remaining amount owed
total = 0
remaining = PRICE

# Loop until the user has inserted enough money
while remaining > 0:
    # Inform the user of the remaining amount due
    print(f"Amount Due: {remaining}")

    # Prompt the user to insert a coin
    coin = int(input("Insert coin: "))

    # Check if the coin is a valid denomination
    if coin in DENOMINATIONS:
        # Add the coin to the total and subtract from the remaining amount owed
        total += coin
        remaining -= coin
    else:
        # Ignore invalid input
        continue

# Calculate the change owed to the user
change = total - PRICE

# Output the change owed to the user
if change > 0:
    print(f"Change Owed: {change}")
else:
    print("Change Owed: 0")
