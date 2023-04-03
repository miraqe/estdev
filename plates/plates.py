def is_valid(s):
    # Check that the plate has at least 2 letters at the start
    if not s[:2].isalpha():
        return False

    # Check that the plate has no punctuation marks
    if any(c in ". ,;:'\"/\\|[]{}()?!@#$%^&*~`" for c in s):
        return False

    # Check that the plate has no more than 6 characters
    if len(s) > 6:
        return False

    # Check that the plate has at least 2 characters
    if len(s) < 2:
        return False

    # Check that the plate has no numbers in the middle
    if any(c.isdigit() for c in s[2:-1]):
        return False

    # Check that the first character after the letters is not a '0'
    if s[2].isdigit() and s[2] == '0':
        return False

    # If all checks pass, the plate is valid
    return True
