fruits = {
    "apple": 130,
    "Avocado": 50,
    "Blackberries": 30,
    "Blueberries": 40,
    "Cantaloupe": 50,
    "Grapefruit": 90,
    "Grapes": 60,
    "Honeydew Melon": 50,
    "kiwifruit": 90,
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
    "sweet cherries": 100,
    "Watermelon": 50,
}

fruit = input("Enter a fruit: ").lower()

if fruit in fruits:
    print("Calories:", fruits[fruit])
