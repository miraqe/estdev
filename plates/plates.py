def is_vanity_plate(s):
    if not s.isalnum():
        return False

    if len(s) < 3 or len(s) > 6:
        return False

    if not s[:2].isalpha():
        return False

    num_count = 0
    for i in range(2, len(s)):
        if s[i].isdigit():
            num_count += 1
            if num_count > 4:
                return False
        elif not s[i].isalpha():
            return False
    return True



def main():
    plate = input("Plate: ")
    if is_vanity_plate(plate):
        print("Valid")
    else:
        print("Invalid")


main()