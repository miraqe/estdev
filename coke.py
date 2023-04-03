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
        # Check if the coin does not exceed the remaining amount owed
        if coin <= remaining:
            # Add the coin to the total and subtract from the remaining amount owed
            total += coin
            remaining -= coin
        else:
            # Inform the user that the coin exceeds the remaining amount owed
            print(f"Change Owed: {remaining}")
    else:
        # Ignore invalid input
        continue

# Calculate the change owed to the user
change = total - PRICE

# Initialize a list to store the coins to be returned as change
coins_to_return = []

# Loop through the denominations and calculate the change
for denomination in DENOMINATIONS:
    while change >= denomination:
        coins_to_return.append(denomination)
        change -= denomination

# Output the change owed to the user
if coins_to_return:
    print("Change Owed: ")
    for coin in coins_to_return:
        print(coin)
else:
    print("Change Owed: 0")
