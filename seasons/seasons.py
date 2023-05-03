from datetime import date
import inflect
import re

p = inflect.engine()

def main():
    days_between = date.today() - check_date()
    print (f"{p.number_to_words(days_between.days *24 * 60)}, minutes")

def check_birthday():
    while True:
        birth_date = input("Enter birthdate: ").strip()
        if re.search(r"(\d{4})-([0-1]\d)-([0-3]\d)$", birth_date):
            return date.fromisoformat(birth_date)
        else:
            print("Invalid Date")

if _name_ == "__main__":
    main()