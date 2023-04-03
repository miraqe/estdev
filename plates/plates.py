def is_valid(s):
    # All vanity plates must start with at least two letters
    if len(s) < 2:
        return False

    # Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters
    if len(s) > 6:
        return False

    # Numbers cannot be used in the middle of a plate; they must come at the end
    if s[2:].isdigit() is False:
        return False

    # The first number used cannot be a ‘0’
    if s[2] == '0':
        return False

    # No periods, spaces, or punctuation marks are allowed
    if any(char.isdigit() or not char.isalnum() for char in s):
        return False

    # All requirements met
    return True


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


if __name__ == '__main__':
    main()
