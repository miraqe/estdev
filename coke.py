# Calculate the remaining amount owed
remaining = PRICE - total

# Inform the user of the remaining amount owed
if remaining > 0:
    print(f"Amount Due: {remaining}")
else:
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
