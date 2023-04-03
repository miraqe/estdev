fruits = {
    "apple": 130,
    "avocado": 50,
    "blackberries": 30,
    "blueberries": 40,
    "cantaloupe": 50,
    "grapefruit": 90,
    "grapes": 60,
    "honeydew Melon": 50,
    "kiwifruit": 90,
    "lemon": 20,
    "lime": 20,
    "mango": 100,
    "nectarine": 70,
    "orange": 80,
    "papaya": 60,
    "peach": 60,
    "pear": 100,
    "pineapple": 80,
    "plum": 70,
    "raspberries": 30,
    "strawberries": 50,
    "sweet cherries": 100,
    "watermelon": 50,
}

fruit = input("Enter a fruit: ").lower()

if fruit in fruits:
    print("Calories:", fruits[fruit])
