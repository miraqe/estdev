grocery_list = {}
try:
    while True:
        item = input("Enter an item for your grocery list: ").lower()
        grocery_list[item] = grocery_list.get(item, 0) + 1
except EOFError:
    pass

print("Grocery List:")
for item, count in sorted(grocery_list.items()):
    print(f"{count} {item.upper()}")
