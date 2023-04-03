import sys

fruit_calories = {
    "Apple": 130,
    "Avocado": 50,
    "Blackberries": 30,
    "Blueberries": 40,
    "Cantaloupe": 50,
    "Grapefruit": 90,
    "Grapes": 60,
    "Honeydew Melon": 50,
    "Kiwifruit": 90,
    "Lemon": 20,
    "Lime": 20,
    "Mango": 100,
    "Nectarine": 70,
    "Orange": 80,
    "Papaya": 60,
    "Peach": 60,
    "Pear": 100,
    "Pineapple": 80,
    "Plum": 70,
    "Raspberries": 30,
    "Strawberries": 50,
    "Sweet Cherry": 100,
    "Watermelon": 50,
}

fruit = input("Enter a fruit: ").lower().replace(" ", "")

if fruit.capitalize() in fruit_calories:
    print("Calories:", fruit_calories[fruit.capitalize()])
else:
    sys.exit()