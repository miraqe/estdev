def is_valid(s):
    # Check length of string
    if len(s) < 2 or len(s) > 6:
        return False

    # Check that first two characters are letters
    if not s[:2].isalpha():
        return False

    # Check that remaining characters are either letters or digits
    if not s[2:].isalnum():
        return False

    # Check that last character is a letter (not a digit)
    if not s[-1].isalpha():
        return False

    # Check that first character is not 0 if the string starts with a digit
    if s[0].isdigit() and s[0] == '0':
        return False

    # All checks passed, so string is valid
    return True
