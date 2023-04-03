def is_vanity_plate(s):
    # Check length of the string
    if len(s) < 2 or len(s) > 6:
        return False
    # Check that first two characters are letters
    if not s[:2].isalpha():
        return False
    # Check that the last characters are digits and not 0
    if not s[2:].isdigit() or s[-1] == '0':
        return False
    return True


def main():
    plate = input("Plate: ")
    if is_vanity_plate(plate):
        print("Valid")
    else:
        print("Invalid")


main()