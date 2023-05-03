from datetime import date, datetime

import sys

def main():
    try:
        print(convert_date(get_birthday()))
    except ValueError:
        sys.exit(1)

def check_birthday():
    return date.fromisoformat(input("Date of Birth?"))

def convert_date(birthday):
    time_passed = date.today() - birthday
    delta = int(timedelta.total_seconds(time_passed) / 60)
    return(f"{p.number_to_words(delta, andword='')} minutes").capitalize()

if _name_ == "__main__":
    main()