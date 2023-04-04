grocery_list = {}
try:
    while True:
        item = input().lower()
        grocery_list[item] = grocery_list.get(item, 0) + 1
except EOFError:
    pass


for item, count in sorted(grocery_list.items()):
    print(f"{count} {item.upper()}")
