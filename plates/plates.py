def is_valid(s):
    # Check that the plate is between 2 and 6 characters long
    if len(s) < 2 or len(s) > 6:
        return False

    # Check that the plate contains only letters and numbers
    if not s.isalnum():
        return False

    # Check that the first two characters are letters
    if not s[:2].isalpha():
        return False

    # Check that the last characters are digits and don't start with 0
    if not s[-1].isdigit() or s[-1] == '0':
        return False

    # Check that there are no digits in the middle of the plate
    if any(char.isdigit() for char in s[2:-1]):
        return False

    # All checks passed, the plate is valid
    return True

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


main()