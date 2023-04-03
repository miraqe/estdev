# Define the price of a bottle of Coke
PRICE = 50

# Define the valid denominations
DENOMINATIONS = [25, 10, 5]

# Initialize the total amount inserted by the user
total = 0

# Loop until the user has inserted enough money
while total < PRICE:
    # Prompt the user to insert a coin
    coin = int(input("Amount Due: (25, 10, or 5): "))

    # Check if the coin is a valid denomination and does not exceed the price of a bottle of Coke
    if coin in DENOMINATIONS and total + coin <= PRICE:
        # Add the coin to the total
        total += coin

        # Inform the user of the amount due
        due = PRICE - total
        if due > 0:
            print(f"Amount Due: {due}")


# Calculate the change owed to the user
change = total - PRICE

# Output the change owed to the user
if change > 0:
    print(f"Change Owed: {change}")
else:
    print("Change Owed: 0")