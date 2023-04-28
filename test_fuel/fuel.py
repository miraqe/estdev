def get_fraction():
    while True:
        fraction = input("Fraction: ")
        try:
            x, y = map(int, fraction.split('/'))
            if y == 0 or x > y:
                raise ValueError
            return x, y
        except (ValueError, ZeroDivisionError):
            continue

def calculate_percentage(x, y):
    percentage = (x / y) * 100
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(round(percentage)) + "%"

if __name__ == "__main__":
    x, y = get_fraction()
    percentage = calculate_percentage(x, y)
    if percentage[-1] == "%":
        percentage = percentage[:-1]
    if percentage == "E":
        print("E")
    elif percentage == "F":
        print("F")
    else:
        print("{}%".format(percentage))
