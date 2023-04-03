def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # remove the leading $
    d = d.replace('$', '')
    # convert to float and return
    return float(d)


def percent_to_float(p):
    # remove the trailing %
    p = p.replace('%', '')
    # divide by 100 to convert from percentage to decimal and return
    return float(p) / 100


main()
