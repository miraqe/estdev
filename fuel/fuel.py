def get_fraction():
    while True:
        fraction = input("Enter a fraction in the format X/Y: ")
        try:
            x, y = map(int, fraction.split('/'))
            if y == 0 or x > y:
                raise ValueError
            return x, y
        except (ValueError, ZeroDivisionError):
            print("Invalid input. Please enter a valid fraction in the format X/Y.")

def calculate_percentage(x, y):
    percentage = (x / y) * 100
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(round(percentage))

if __name__ == "__main__":
    while True:
        x, y = get_fraction()
        percentage = calculate_percentage(x, y)
        print("{}%".format(percentage))
        if percentage == "E" or percentage == "F":
            break
