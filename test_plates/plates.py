

def is_valid(s):
    # Check that the string has at least 2 characters and at most 6 characters
    if len(s) < 2 or len(s) > 6:
        return False

    # Check that the string contains only letters
    if s[0].isalpha() == False or s[1].isalpha == False:
        return False

    # Check that there are no letters after the numbers
    if s[-1].isalpha():
        return False
    for i in range(len(s) - 2):
        if s[i].isdigit() and s[i+1].isdigit() and s[i+2].isalpha():
            return False

    # Check that the first character of the number sequence is not '0'
    num_start = -1
    for i in range(2, len(s)):
        if s[i].isdigit():
            num_start = i
            if s[i] == '0' and i != len(s)-1:
                return False
            else:
                break

    # If there are no numbers in the string, it is valid
    if num_start == -1:
        return True

    # Check that all characters after the first number are also numbers
    for i in range(num_start+1, len(s)):
        if not s[i].isdigit():
            return False

    # If all checks pass, the vanity plate is valid
    return True



def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


main()