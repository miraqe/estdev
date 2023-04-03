# Create a dictionary to store the fruits and their calorie information
fruits = {
    "Apple": 130,
    "Avocado": 50,
    "Blackberries": 60,
    "Blueberries": 80,
    "Cantaloupe": 50,
    "Cherries": 90,
    "Grapefruit": 60,
    "Grapes": 60,
    "Honeydew Melon": 50,
    "Kiwi": 90,
    "Mango": 135,
    "Nectarine": 60,
    "Orange": 80,
    "Papaya": 60,
    "Peach": 60,
    "Pear": 100,
    "Pineapple": 80,
    "Plums": 70,
    "Raspberries": 60,
    "Strawberries": 50
}

# Get the user input and convert it to lowercase
fruit = input().lower()

# Check if the user input matches a fruit in the dictionary
if fruit in fruits:
    # If the fruit is in the dictionary, print its calorie information
    print("Calories:", fruits[fruit])
else:
    # If the fruit is not in the dictionary, print nothing
    pass
