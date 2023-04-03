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
