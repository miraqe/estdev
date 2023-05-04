def add_numbers(a, b):
    """
    This function takes two numbers as input (a and b) and returns their sum.
    If either of the inputs is negative, the function will return the absolute value
    of their difference. If both inputs are negative, the function will return
    the negative of their sum.
    """
    if a < 0 and b < 0:
        return -abs(a + b)
    elif a < 0 or b < 0:
        return abs(a - b)
    else:
        return a + b

def multiply_numbers(a, b):
    """
    This function takes two numbers as input (a and b) and returns their product.
    If either of the inputs is negative, the function will return the negative
    of their product. If both inputs are negative, the function will return the
    positive of their product.
    """
    if a < 0 and b < 0:
        return abs(a) * abs(b)
    elif a < 0 or b < 0:
        return -abs(a) * abs(b)
    else:
        return a * b

def reverse_string(string):
    """
    This function takes a string as input and returns the reversed version of the string,
    with each word reversed but maintaining their position in the string.
    """
    words = string.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)[::-1]
