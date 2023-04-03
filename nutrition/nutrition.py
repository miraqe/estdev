# Create a dictionary of fruits and their calories per portion
fruit_calories = {
    "Apple": 130,
    "Apricot": 17,
    "Avocado": 50,
    "Banana": 105,
    "Blackberry": 62,
    "Blueberry": 57,
    "Cantaloupe": 60,
    "Cherry": 50,
    "Clementine": 35,
    "Coconut meat": 283,
    "Grapes": 52,
    "Guava": 37,
    "Honeydew melon": 64,
    "Kiwi": 46,
    "Mango": 135,
    "Nectarine": 70,
    "Orange": 70,
    "Papaya": 120,
    "Peach": 59,
    "Pear": 100,
    "Pineapple": 82,
    "Plum": 46,
    "Raspberries": 64,
    "Strawberries": 49,
    "Sweet Cherries": 100,
    "Watermelon": 46
}

# Take input from the user
fruit = input("Enter a fruit: ")

# Convert the input to lowercase for case-insensitivity
fruit = fruit.lower()

# Check if the input fruit is in the dictionary and print its calories if it is
if fruit in fruit_calories:
    print("Calories: ", fruit_calories[fruit])
