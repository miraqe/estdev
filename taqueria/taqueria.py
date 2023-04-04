MENU = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    total_cost = 0.0
    while True:
        try:
            item = input("Item: ").strip().title()
        except EOFError:
            break
        if item not in MENU:
            continue
        cost = MENU[item]
        total_cost += cost
        print("${:.2f}".format(total_cost))

if __name__ == "__main__":
    main()
