def is_vanity_plate(plate):
    # check that plate has at least 2 and at most 6 characters
    if not 2 <= len(plate) <= 6:
        return "Invalid"

    # check that first 2 characters are letters
    if not plate[:2].isalpha():
        return "Invalid"

    # check that the last characters are digits
    if not plate[-4:].isdigit():
        return "Invalid"

    # check that there are no letters after the numbers
    if plate[-3:].isalpha():
        return "Invalid"

    # check that the first digit is not 0 if it's in position 3
    if len(plate) >= 4 and plate[2].isdigit() and plate[2] == '0':
        return "Invalid"

    # check that the first digit is not 0 if it's in position 4 or 5
    if len(plate) >= 5 and plate[3].isdigit() and plate[3] == '0':
        return "Invalid"

    # check that there are no numbers in between letters
    for i in range(2, len(plate)-4):
        if plate[i].isdigit() or plate[i+1].isdigit():
            return "Invalid"

    # if all checks pass, return "Valid"
    return "Valid"



def main():
    plate = input("Plate: ")
    if is_vanity_plate(plate):
        print("Valid")
    else:
        print("Invalid")


main()