def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[:-1].isalpha() or not s[-1].isdigit():
        return False
    if s[0] == '0':
        return False
    return True
