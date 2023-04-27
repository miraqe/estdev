import inflect

p = inflect.engine()

names = []
while True:
    try:
        name = input()
    except EOFError:
        break
    names.append(name)

num_names = len(names)

if num_names == 1:
    print(f"Adieu, adieu, to {names[0]}")
elif num_names == 2:
    print(f"Adieu, adieu, to {names[0]} and {names[1]}")
else:
    name_str = ", ".join(names[:-1])
    print(f"Adieu, adieu, to {name_str}, and {names[-1]}")
