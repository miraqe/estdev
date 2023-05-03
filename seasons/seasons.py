from datetime import date
import sys
import re
# pip imported library to convert numbers into word format
from num2words import num2words


def main():
    print(convert(input("Date of Birth: ")))


def convert(dob):
    # Validates user input
    if re.search(r'^([1-2][0-9][0-9][0-9])-([0-1][0-9])-([0-3][0-9])$', dob):
        today = date.today()
        try:
            # Validate date format
            input_date = date.fromisoformat(dob)
        except ValueError:
            sys.exit("Invalid Date")
    # Calulations
    minus = today - input_date
    calculation = minus.days * 24 * 60
    word_form = num2words(calculation)

    # removes the word 'and'
    final = re.sub(r' and', '', word_form)

    return f'{final.capitalize()} minutes'

else:
    sys.exit("Invalid Date")


if __name__ == "__main__":
    main()