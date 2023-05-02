def main():
    while True:
        try:
            fraction = input("Fraction: ")
            print(gauge(convert(fraction)))
            return 0
        except (ValueError,ZeroDivisionError):
            continue

def convert(s):
    try:
        x, y = map(int, s.split("/"))
        if y == 0:
            raise ZeroDivisionError
        percent = round((x / y) * 100)
        if percent < 0 or percent > 100:
            raise ValueError
        return percent
    except (ValueError, ZeroDivisionError):
        raise ValueError




def gauge(x):
    if x <= 1:
        return "E%"
    elif x >= 99:
        return "F%"
    else:
        return "{}%".format(x)


if __name__ == "__main__":
    main()


"""def main():
    fraction = input("Fraction: ")
    fraction_converted = convert(fraction)
    output = gauge(fraction_converted)
    print(output)

def convert(fraction):
    while True:
        try:
            numerator, denominator = fraction.split("/")
            new_numerator = int(numerator)
            new_denominator = int(denominator)
            f = new_numerator / new_denominator
            if f >=1:
                p = int(f * 100)
                return p
            else:
                fraction = input("Fraction: ")
                pass
        except (ValueError, ZeroDivisionError):
            raise

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"

if __name__ == "__main__":
    main()
"""