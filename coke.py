# Define the price of a bottle of Coke
PRICE = 50

# Define the valid denominations
DENOMINATIONS = [25, 10, 5]

# Initialize the total amount inserted by the user
total = 0

# Loop until the user has inserted enough money
while total < PRICE:
    # Inform the user of the amount due
    due = PRICE - total
    print(f"Amount Due: {due}")

    # Prompt the user to insert a coin
    coin = int(input("Insert coin: "))

    # Check if the coin is a valid denomination and does not exceed the price of a bottle of Coke
    if coin in DENOMINATIONS and total + coin <= PRICE:
        # Add the coin to the total
        total += coin
    else:
        # Inform the user that the coin is invalid or exceeds the price of a bottle of Coke
        print("Invalid coin. Please insert a valid coin.")

# Calculate the change owed to the user
change = total - PRICE

# Output the change owed to the user
if change > 0:
    print(f"Change Owed: {change}")
else:
    print("Change Owed: 0")

