def is_vanity_plate(s):
    # Check that the length is between 2 and 6 characters
    if len(s) < 2 or len(s) > 6:
        return False

    # Check that first two characters are letters
    if not s[:2].isalpha():
        return False

    # Check that the remaining characters are alphanumeric
    if not s[2:].isalnum():
        return False

    # Check that the first character of the number sequence is not '0'
    if s[2:].isdigit() and s[2] == '0':
        return False

    # Check that the number sequence is at most 4 characters long
    if s[2:].isdigit() and len(s[2:]) > 4:
        return False

    # If all checks pass, return True
    return True


def main():
    plate = input("Plate: ")
    if is_vanity_plate(plate):
        print("Valid")
    else:
        print("Invalid")


main()