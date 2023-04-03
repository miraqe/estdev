def is_valid_vanity_plate(s):
    # Check length is between 2 and 6 characters
    if not (2 <= len(s) <= 6):
        return False

    # Check that first two characters are letters
    if not s[:2].isalpha():
        return False

    # Check that last characters are digits and not starting with 0
    if not s[-4:].isdigit() or s[-4:].startswith('0'):
        return False

    # Check that digits do not appear in the middle of the string
    for i in range(2, len(s)-4):
        if s[i].isdigit():
            return False

    # Otherwise, the string is valid
    return True

def main():
    plate = input("Plate: ")
    if is_valid_vanity_plate(plate):
        print("Valid")
    else:
        print("Invalid")


main()