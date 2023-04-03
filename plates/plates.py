def is_vanity_plate(s):
    # Check that the string has at least 2 characters and at most 6 characters
    if len(s) < 2 or len(s) > 6:
        return False

    # Check that first two characters are letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    # Check that there are no letters after the numbers
    if s[-1].isalpha():
        return False
    for i in range(len(s) - 2):
        if s[i].isdigit() and s[i+1].isdigit() and s[i+2].isalpha():
            return False

    # Check that the first character of the number sequence is not '0'
    num_flag = False
    for i in range(2, len(s)):
        if s[i].isdigit():
            if s[i] == '0' and i != len(s)-1:
                return False
            else:
                num_flag = True
                break

    # Check that there are no letters between the first and last digits
    if num_flag:
        num_start = s.index([c for c in s if c.isdigit()][0])
        num_end = s.rindex([c for c in s if c.isdigit()][-1])
        if any(char.isalpha() for char in s[num_start:num_end+1]):
            return False

    # If all checks pass, the vanity plate is valid
    return True



def main():
    plate = input("Plate: ")
    if is_vanity_plate(plate):
        print("Valid")
    else:
        print("Invalid")


main()