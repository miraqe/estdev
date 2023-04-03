def is_vanity_plate(s):
    # Check length
    if len(s) < 2 or len(s) > 6:
        return False

    # Check that first two characters are letters
    if not s[:2].isalpha():
        return False

    # Check that last characters are digits
    if not s[-4:].isdigit():
        return False

    # Check that first character of number sequence is not '0'
    index = 2
    while index < len(s) and s[index].isalpha():
        index += 1
    if index < len(s) and s[index] == '0':
        return False

    return True


def main():
    plate = input("Plate: ")
    if is_vanity_plate(plate):
        print("Valid")
    else:
        print("Invalid")


main()